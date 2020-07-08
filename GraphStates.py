# First attempts at working with dataset in Python
# Read in from https://github.com/nytimes/covid-19-data

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.dates import DateFormatter
import pandas as pd
import git
import numpy as np
from pandas.plotting import register_matplotlib_converters
from datetime import datetime

register_matplotlib_converters()

# extract date, cases, and deaths for matching State string in target
def getStateInfo(targetState, filename):
    stateData = pd.read_csv(filename)
    dates = stateData.date.copy()
    allCases = stateData.cases.copy()
    allDeaths = stateData.deaths.copy()
    states = stateData.state.copy()
    counts = np.count_nonzero(states == targetState)

    stateDates = [0] * counts
    stateCases = [0] * counts
    stateDeaths = [0] * counts

    insertionPoint = 0

    for index, item in enumerate(states):
        if item == targetState:
            stateDates[insertionPoint] = dates[index]
            stateCases[insertionPoint] = allCases[index]
            stateDeaths[insertionPoint] = allDeaths[index]
            insertionPoint += 1

    return [stateDates, stateCases, stateDeaths]

# calculate rise in cases day/day
def calcNewCases(totalCases):
    newCases = [0] * len(totalCases)

    for x in range(1, len(totalCases)):
        newCases[x] = totalCases[x] - totalCases[x - 1]

    return newCases

# smooth data over set window size in days
def movingAverage(windowSize, data):
    kernel = [1 / windowSize] * windowSize
    cutoff = len(data)
    fullConvolution = np.convolve(data, kernel, "full")
    return fullConvolution[0:cutoff]

# plot state data for all states in list, smoothed over window size in days
def graphStates(stateList, integrationTime):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    for state in stateList:
        [stateDates, stateCases, stateDeaths] = getStateInfo(state,'/Users/arnabchatterjee/pycharmprojects/covid-19_analysis/venv/covid-19-data/us-states.csv')
        stateDates = pd.to_datetime(stateDates)
        stateNewCases = calcNewCases(stateCases)
        stateNewCases = movingAverage(integrationTime, stateNewCases)

        ax.plot(stateDates, stateNewCases)
    plt.title(f"New Covid-19 Cases by US State, {integrationTime}-Day Average")
    matplotlib.dates.DayLocator(bymonthday=1, interval=30)

    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend(stateList)

    myFmt = DateFormatter("%m/%d")
    ax.xaxis.set_major_formatter(myFmt)

    fig.autofmt_xdate()

    plt.show()

# targetStates = ["New York","New Jersey","California","Texas"]
# targetStateIndex = 0
#
# #graphStates(targetStates, 7)
#
# state_populations= pd.read_csv('/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_populations.csv')
# states_for_population = state_populations.state.copy()
# population_2019 = state_populations.population_2019.copy()
#
# for target in targetStates:
#     index = list(np.where(states_for_population == target)[0])
#     plt.bar(states_for_population[index], population_2019[index])
# plt.show()

def loadStateData(stateList):
    state_populations = pd.read_csv(
        '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_populations.csv')
    states_for_population = state_populations.state.copy()
    population_2019 = state_populations.population_2019.copy()

    for target in targetStates:
        index = list(np.where(states_for_population == target)[0])
        plt.bar(states_for_population[index], population_2019[index])
    plt.show()
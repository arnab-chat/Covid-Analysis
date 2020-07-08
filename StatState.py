# creating class to contain State Data

import pandas as pd
import datetime
import numpy as np
from matplotlib import dates

class StatState:

    population_2019 = None
    covid19_dates = None
    covid19_cases = None
    covid19_deaths = None
    covid19_new_cases = None

    def __init__(self, name):
        self.name = name

    def __init__(self, name,covid_filename,population_filename):
        self.name = name
        self.get_covid_info(covid_filename)
        self.get_population_info(population_filename)

    def calc_new_cases(self):
        self.covid19_new_cases = [0] * len(self.covid19_cases)

        for x in range(1, len(self.covid19_cases)):
            self.covid19_new_cases[x] = self.covid19_cases[x] - self.covid19_cases[x - 1]

    def get_covid_info(self, filename):
        # read from file
        all_covid_data = pd.read_csv(filename)

        # separate columns
        all_dates = all_covid_data.date.copy()
        all_cases = all_covid_data.cases.copy()
        all_deaths = all_covid_data.deaths.copy()
        all_states = all_covid_data.state.copy()

        # determine number of entries for particular state
        counts = np.count_nonzero(all_states == self.name)

        # resize lists
        self.covid19_dates = [0] * counts
        self.covid19_cases = [0] * counts
        self.covid19_deaths = [0] * counts

        # variable to track index of where next state entry should be added from all_covid_data pd
        insertionPoint = 0

        # find matching data for state and load
        for index, item in enumerate(all_states):
            if item == self.name:
                self.covid19_dates[insertionPoint] = all_dates[index]
                self.covid19_cases[insertionPoint] = all_cases[index]
                self.covid19_deaths[insertionPoint] = all_deaths[index]
                insertionPoint += 1
        # calculate new cases
        self.calc_new_cases()
        self.covid19_dates = pd.to_datetime(self.covid19_dates)

    def get_population_info(self,filename):
        state_populations = pd.read_csv(filename)
        states_for_population = state_populations.state.copy()
        population_2019 = state_populations.population_2019.copy()
        index = list(np.where(states_for_population == self.name)[0])
        self.population_2019 = int(population_2019[index])

    def movingAverage(windowSize, data):
        kernel = [1 / windowSize] * windowSize
        cutoff = len(data)
        fullConvolution = np.convolve(data, kernel, "full")
        return fullConvolution[0:cutoff]
from StatState import *
import matplotlib
from matplotlib import dates
from StatRegion import *
from GraphStates import *
from matplotlib import pyplot as plt

# source file paths
population_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_populations.csv'
covid19_state_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-states.csv'
covid19_national_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us.csv'
covid19_county_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv'

# general variables
window_size = 7

# regions to track
NYC = StatRegion("New York City", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')

plt.plot(NYC.covid19_dates,NYC.covid19_new_cases)
plt.show()
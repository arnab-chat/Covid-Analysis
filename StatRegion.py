# creating class to contain custom region Data

import pandas as pd
from pandas import datetime
import datetime
import numpy as np
from matplotlib import dates
import os

class StatRegion:

    covid19_dates = None
    covid19_cases = None
    covid19_deaths = None
    covid19_new_cases = None
    containing_state = ""

    def __init__(self, county, state, covid_filename):
        self.name = county
        self.containing_state = state
        self.get_covid_info(covid_filename)

    def get_covid_info(self, filename):
        # read from file
        all_covid_data = pd.read_csv(filename)

        # separate columns
        all_dates = all_covid_data.date.copy()
        all_cases = all_covid_data.cases.copy()
        all_deaths = all_covid_data.deaths.copy()
        #all_states = all_covid_data.states.copy()
        all_counties = all_covid_data.county.copy()
        all_fips = all_covid_data.fips.copy()




        # variable to track index of where next state entry should be added from all_covid_data pd
        insertionPoint = 0
        counts = 0
        columns = all_covid_data.iteritems()
        date_col = next(columns)
        county_col = next(columns)
        state_col = next(columns)
        fips_col = next(columns)
        cases_col = next(columns)
        deaths_col = next(columns)

        for row_index in range(0,len(county_col[1])-1):
            if county_col[1][row_index] == self.name and state_col[1][row_index] == self.containing_state:
                counts += 1

        # resize lists
        self.covid19_dates = [0] * counts
        self.covid19_cases = [0] * counts
        self.covid19_deaths = [0] * counts

        print(f"Retrieving {counts} entries for {self.name}, {self.containing_state}")

        for row_index in range(0,len(county_col[1])-1):
            if county_col[1][row_index] == self.name and state_col[1][row_index] == self.containing_state:
                self.covid19_dates[insertionPoint] = date_col[1][row_index]
                self.covid19_cases[insertionPoint] = cases_col[1][row_index]
                self.covid19_deaths[insertionPoint] = deaths_col[1][row_index]
                insertionPoint += 1
            # if row_index % 20000 == 0:
            #     print(f"{np.int(round(row_index/len(county_col[1])*100))}% complete")

        self.covid19_dates = pd.to_datetime(self.covid19_dates)
        self.calc_new_cases()
    def calc_new_cases(self):
        self.covid19_new_cases = [0] * len(self.covid19_cases)

        for x in range(1, len(self.covid19_cases)):
            self.covid19_new_cases[x] = self.covid19_cases[x] - self.covid19_cases[x - 1]
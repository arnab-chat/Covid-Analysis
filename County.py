# creating class to contain county Data

import pandas as pd
import numpy as np
from pandas import datetime
import datetime

class County:

    covid19_dates = None
    covid19_cases = None
    covid19_deaths = None
    covid19_new_cases = None
    containing_state = None

    def __init__(self, county, state, covid_filename):
        self.name = county
        self.containing_state = state
        self.get_covid_info(covid_filename)

    def get_covid_info(self, filename):
        # read from file
        all_covid_data = pd.read_csv(filename)

        # separate columns
        all_dates = list(all_covid_data.date)
        all_cases = list(all_covid_data.cases)
        all_deaths = list(all_covid_data.deaths)
        all_states = list(all_covid_data.state)
        all_counties = list(all_covid_data.county)
        all_fips = list(all_covid_data.fips)

        # determine number of entries for target county, pre-initialize lists to right size

        entries_in_county = 0

        for county, state in zip(all_counties, all_states):
            if county == self.name and state == self.containing_state:
                entries_in_county += 1

        self.covid19_dates = [0] * entries_in_county
        self.covid19_cases = [0] * entries_in_county
        self.covid19_deaths = [0] * entries_in_county
        self.covid19_new_cases = [0] * entries_in_county

        # load data into object variables
        entry_location = iter(range(0,entries_in_county))

        for county, state, date, cases, deaths in zip(all_counties, all_states, all_dates, all_cases, all_deaths):
            if county == self.name and state == self.containing_state:
                index = next(entry_location)
                self.covid19_dates[index] = date
                self.covid19_cases[index] = cases
                self.covid19_deaths[index] = deaths

        # calculate new cases
        yesterdays_cases = (self.covid19_cases[:-1])
        yesterdays_cases.insert(0, 0)
        self.covid19_new_cases = np.asarray(self.covid19_cases) - np.asarray(yesterdays_cases)
        self.covid19_new_cases[0] = 0

        # format dates
        self.covid19_dates = pd.to_datetime(self.covid19_dates)

        print(f"Loaded data for {self.name} County, {self.containing_state}")

    def moving_average(self,window_size):
        kernel = [1/window_size]*window_size
        self.covid19_cases = np.convolve(self.covid19_cases,kernel,'same')
        self.covid19_deaths = np.convolve(self.covid19_deaths, kernel, 'same')
        self.covid19_new_cases = np.convolve(self.covid19_new_cases, kernel, 'same')


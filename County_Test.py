from matplotlib.dates import DateFormatter
import matplotlib
from matplotlib import pyplot as plt
from County import *
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
# source file paths
# Read in from https://github.com/nytimes/covid-19-data
population_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_populations.csv'
covid19_state_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-states.csv'
covid19_national_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us.csv'
covid19_county_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv'
state_abbrs = pd.read_csv('/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_abbr.csv')

# # load national data
# national_data = pd.read_csv(covid19_county_data_source_file)
#
# national_dates = pd.to_datetime(national_data.date)
# national_cases = national_data.cases
# national_deaths = national_data.deaths


window_size = 14

austin = County("Travis", "Texas", covid19_county_data_source_file)
nyc = County("New York City", "New York", covid19_county_data_source_file)
houston = County("Harris", "Texas", covid19_county_data_source_file)

# figure appearance
plt.style.use('ggplot')
fig, ax = plt.subplots()
plt.title(f"New Covid-19 Cases, {window_size}-Day Average")
matplotlib.dates.DayLocator(bymonthday=1, interval=14)
plt.xlabel("Date")
plt.ylabel("New Cases")
ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))
fig.autofmt_xdate()


#houston.moving_average(window_size)
#ax.bar(nyc.covid19_dates,nyc.covid19_new_cases)
ax.bar(houston.covid19_dates,houston.covid19_new_cases)
#ax.plot(nyc.covid19_dates,nyc.covid19_new_cases)
plt.show()
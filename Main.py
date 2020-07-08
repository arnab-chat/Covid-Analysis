from StatState import *
from GraphStates import *
import matplotlib
from matplotlib import dates
from matplotlib import pyplot as plt
from StatRegion import *

register_matplotlib_converters()

# source file paths
# Read in from https://github.com/nytimes/covid-19-data
population_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_populations.csv'
covid19_state_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-states.csv'
covid19_national_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us.csv'
covid19_county_data_source_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv'
state_abbrs = pd.read_csv('/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/state_abbr.csv')

# general variables
window_size = 1
track_state_codes = ["NY", "TX", "FL", "CA", "MO","TN"]
#track_state_names = [0]*len(track_state_codes)
track_state_names = []

# states to track, manual Pythonic way
# NY = StatState("New York", covid19_state_data_source_file, population_source_file)
TX = StatState("Texas", covid19_state_data_source_file, population_source_file)
# FL = StatState("Florida", covid19_state_data_source_file, population_source_file)
# CA = StatState("California", covid19_state_data_source_file, population_source_file)



for given_code in track_state_codes:
    for code in state_abbrs.Code:
        if code == given_code:
            track_state_names.append(state_abbrs.State[list(state_abbrs.Code).index(given_code)])

print(track_state_names)

# for state, code in zip(track_state_names,track_state_codes):
#     exec(code + " = StatState(\"" + state + "\",\'" + covid19_state_data_source_file + "\',\'" + population_source_file + "\')")

# # regions to track
# #NYC = StatRegion("New York City","New York", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
# Houston = StatRegion("Harris", "Texas", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
# Austin = StatRegion("Travis", "Texas", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
# LA = StatRegion("Los Angeles", "California", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
# Dallas = StatRegion("Dallas", "Texas", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
# Miami = StatRegion("Miami-Dade", "Florida", '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/us-counties.csv')
#
#
# figure appearance
plt.style.use('ggplot')
fig, ax = plt.subplots()
plt.title(f"New Covid-19 Cases, {window_size}-Day Average")
matplotlib.dates.DayLocator(bymonthday=1, interval=14)
plt.xlabel("Date")
plt.ylabel("New Cases")
myFmt = DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
#
# # plot states
# # ax.plot(NY.covid19_dates, movingAverage(window_size,NY.covid19_new_cases))
ax.bar(TX.covid19_dates, movingAverage(window_size,TX.covid19_new_cases))
# #ax.plot(FL.covid19_dates, movingAverage(window_size,FL.covid19_new_cases))
# # ax.plot(CA.covid19_dates, movingAverage(window_size,CA.covid19_new_cases))
#
# #plot regions
# #NY - NYC
# #ax.plot(NY.covid19_dates, movingAverage(window_size, np.asarray(NY.covid19_new_cases) - np.asarray(NYC.covid19_new_cases)))
# #ax.plot(NYC.covid19_dates,movingAverage(window_size,NYC.covid19_new_cases))
#
# ax.plot(Miami.covid19_dates,movingAverage(window_size,Miami.covid19_new_cases))
# ax.plot(Houston.covid19_dates,movingAverage(window_size,Houston.covid19_new_cases))
# ax.plot(Austin.covid19_dates,movingAverage(window_size,Austin.covid19_new_cases))
# ax.plot(Dallas.covid19_dates,movingAverage(window_size,Dallas.covid19_new_cases))
# ax.plot(LA.covid19_dates,movingAverage(window_size,LA.covid19_new_cases))
#
# ax.legend(['Miami-Dade','Houston (Harris)','Austin (Travis)','LA','Dallas'])
plt.xlim(737500.75, 737616.25)
plt.show()

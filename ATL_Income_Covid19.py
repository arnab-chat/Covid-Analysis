import pandas as pd

income_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/ATL_Income_2016_Formatted.csv'
covid19_file = '/Users/arnabchatterjee/PycharmProjects/Covid-19_Analysis/venv/covid-19-data/ATL_cases_by_county.csv'

income_data = pd.read_csv(income_file)
covid_data = pd.read_csv(covid19_file)

income_county_col = income_data.County
pct_hhi_under35k = income_data.Pct_HH_income_less_35k
pct_hhi_35kto75k = income_data.Pct_HH_income_35k_75k
pct_hhi_75kto200k = income_data.Pct_HH_income_75k_200k
pct_hhi_over200k = income_data.Pct_HH_income_200k_more

covid_county_col = covid_data.county_resident
covid_cases = covid_data.Positive

counties_atl = income_county_col.unique()

rows_income = income_data.iterrows()

header = next(rows_income)

#print(header)

print(next(rows_income))
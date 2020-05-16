import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from util import country_vs_date

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
total_confirmed = country_vs_date(confirmed).Total

deaths = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
total_deaths = country_vs_date(deaths).Total

recovered = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
total_recovered = country_vs_date(recovered).Total

fig, ax = plt.subplots(figsize=(8, 8))
total_confirmed.plot(ax=ax, label="Confirmed")
plt.fill_between(total_confirmed.index, total_confirmed.values)
total_recovered.plot(ax=ax, label="Recovered")
plt.fill_between(total_confirmed.index, total_recovered.values)
total_deaths.plot(ax=ax, label="Deaths")
plt.fill_between(total_confirmed.index, total_deaths.values)
freq = 3
# setting xticks = the dates with the frequency of 3, and setting them vertical, any df.index works since they are the same
plt.xticks(np.arange(0, len(total_confirmed.index), step=freq),
           total_confirmed.index[::freq], rotation=-90)
plt.title(
    "Time series of total number of confirmed cases, deaths and people recovered")
plt.xlabel("Dates")
plt.ylabel("Number")
# disable scientific notation
plt.ticklabel_format(style='plain', axis='y')
plt.grid(linestyle="--")
plt.legend(loc="upper left")
plt.show()

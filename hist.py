import pandas as pd
import matplotlib.pyplot as plt
from util import country_vs_date
import numpy as np

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)
fig, ax = plt.subplots()
# Remove Total column, transpose it to make countries as index and we get the last column which is the latest date
confirmed_per_country = confirmed.drop(columns=["Total"]).T.iloc[:, -1]
xticks = np.arange(0, 600001, 50000)
confirmed_per_country.hist(bins=xticks, ax=ax)
# Set up xticks and yticks interval
ax.set_xticks(xticks, minor=True)
ax.set_yticks(np.arange(0, 181, 5), minor=True)
# Set up grid alpha level
ax.grid(which="minor", alpha=0.2)
ax.grid(which="major", alpha=0.5)
plt.title("Number of confirmed cases till 12/4/2020")
plt.xlabel("Number of confirmed cases")
plt.ylabel("Number of countries")
plt.show()

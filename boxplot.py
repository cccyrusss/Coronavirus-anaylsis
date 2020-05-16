import matplotlib.pyplot as plt
import pandas as pd
from util import country_vs_date
import seaborn as sns
import calendar
import numpy as np

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)
# convert string index to date time index
confirmed.index = pd.to_datetime(confirmed.index)

# compute new cases dataframe by substracting the number of confirmed cases of prev day
new_cases = confirmed.diff().fillna(confirmed)
new_cases["Month"] = new_cases.index.month
new_cases["Month"] = new_cases["Month"].apply(
    lambda x: calendar.month_abbr[x])
fig, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(y="Total", x="Month",
            data=new_cases, ax=ax)
# Set title
ax.set_title("Total new confiremd cases per day")
ax.set_ylabel("Total new confiremd cases")
# Set up minor yticks
ax.set_yticks(np.arange(0, 100001, 4000), minor=True)
# Set grid opacity
ax.grid(which="minor", alpha=0.2)
ax.grid(which="major", alpha=0.5)
plt.show()

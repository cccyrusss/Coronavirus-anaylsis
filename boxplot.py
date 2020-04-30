import matplotlib.pyplot as plt
import pandas as pd
from util import country_vs_date
import seaborn as sns
import calendar

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)
confirmed.index = pd.to_datetime(confirmed.index)

new_cases = confirmed.diff().fillna(confirmed)
new_cases["Month"] = new_cases.index.month
new_cases["Month"] = new_cases["Month"].apply(
    lambda x: calendar.month_abbr[x])
fig, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(y="Total", x="Month",
            data=new_cases, ax=ax)
ax.set_title("Total new confiremd cases per day")
ax.set_ylabel("Total new confiremd cases")

# months = new_cases.month.unique()
# fig, axes = plt.subplots(2, 2)
# for i, month in enumerate(months):
#     sns.boxplot(y="Total", x="month",
#                 data=new_cases[new_cases.month == month], ax=axes[int(i/2)][i % 2])
# fig.tight_layout()
plt.show()
# for month in months:

# sns.boxplot(y="Total", x="month", data=new_cases[new_cases.month == 1])
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
from util import country_vs_date


def bar_plot(df, ax):
    df.plot.bar(ax=ax)
    plt.gca().get_legend().remove()
    plt.show()


confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)
confirmed_sorted = confirmed.sort_values(
    confirmed.last_valid_index(), axis=1, ascending=False)

fig, ax = plt.subplots(figsize=(15, 8))
# bar chart of confirmed cases amongst countries (top 20)
bar_plot(confirmed_sorted.iloc[:, :40].drop(
    columns=["Total", "US"]).tail(1).T, ax)

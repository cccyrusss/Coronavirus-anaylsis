import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Code runs here
def main():
    confirmed = pd.read_csv(
        "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    confirmed = convert(confirmed)
    confirmed_top_10 = confirmed.iloc[:, :12] # top 10 including "Total"
    # Total confirmed cases
    plot(confirmed_top_10.loc[:, "Total"], "Time series of total confirmed cases",
         "Dates", "Number of confirmed cases")
    # Confirmed cases except total
    plot(confirmed_top_10.drop(columns=[
         "Total"]), "Time series of confirmed cases amongst countries", "Dates", "Number of confirmed cases")
    # New cases of confirmed cases (only includes Total and 10 countries having the highest confirmed cases)
    new_cases = confirmed_top_10.diff().fillna(confirmed)
    plot(new_cases, "New confirmed cases in global", "Dates", "New confirmed cases")
    # bar chart of confirmed cases amongst countries (top 20)
    bar_plot(confirmed.iloc[:, :20].drop(columns=["Total"]).tail(1).T)

# filter data


def filter(df):
    df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
    df = df.groupby("Country/Region").sum()
    return df

# Convert time-series dataframe to a specific format


def convert(df):
    df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
    df = df.groupby("Country/Region").sum()
    df.loc["Total"] = df.sum()
    df = df.sort_values(df.columns[-1], ascending=False)
    return df.T


# Plot the graph
def plot(df, title, xlabel, ylabel):
    freq = 3
    df.plot(figsize=(12, 8))
    plt.xticks(np.arange(0, len(df.index), step=freq),
               df.index[::freq], rotation=-90)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def bar_plot(df):
    df.plot.bar()
    plt.gca().get_legend().remove()
    plt.show()


if __name__ == "__main__":
    main()

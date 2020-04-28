import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Code runs here
def main():
    confirmed = pd.read_csv(
        "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    confirmed_top_10 = convert(confirmed).iloc[:, :12]
    print(confirmed_top_10)
    # Total confirmed cases
    plot(confirmed_top_10.loc[:, "Total"], "Time series of total confirmed cases",
         "Dates", "Number of confirmed cases")
    # Confirmed cases except total
    plot(confirmed_top_10.drop(columns=[
         "Total"]), "Time series of confirmed cases amongst countries", "Dates", "Number of confirmed cases")
    # bar_plot(confirmed.drop(columns=["Total"]).tail(1).T)

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

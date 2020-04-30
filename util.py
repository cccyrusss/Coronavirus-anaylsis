import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Convert time-series dataframe to a specific format (Country vs date)
def country_vs_date(df):
    df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
    df = df.groupby("Country/Region").sum()
    df.loc["Total"] = df.sum()
    # df = df.sort_values(df.columns[-1], ascending=False)
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

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from util import country_vs_date
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as mtick
import seaborn as sns

confirmed = country_vs_date(pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"))

deaths = country_vs_date(pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"))

recovered = country_vs_date(pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"))

# Computing death rate and recovery rate
death_rate = (deaths*100).div(confirmed).fillna(0)
death_rate = death_rate.T.reset_index().rename(
    columns={"Country/Region": "Country", "4/12/20": "Death rate"})
death_rate = death_rate.iloc[:, [0, -1]]

recovery_rate = (recovered*100).div(confirmed).fillna(0)
recovery_rate = recovery_rate.T.reset_index().rename(
    columns={"Country/Region": "Country", "4/12/20": "Recovery rate"})
recovery_rate = recovery_rate.iloc[:, [0, -1]]

# Processing human development data
human_dev = pd.read_excel(
    "data/Human Development Index/hdro_statistical_data_tables_1_15_d1_d5.xlsx", header=5, usecols="A:C,E")
human_dev = human_dev.drop(index=[0, 1])
human_dev = human_dev.rename(
    {"(index value)": "HDI", "(years)": "Life Expectancy"}, axis=1)
human_dev.set_index("HDI rank", inplace=True)
human_dev = human_dev.dropna(axis=0)
human_dev = human_dev.iloc[:189, :]

# Merge with death_rate
merged = pd.merge(death_rate, human_dev, on="Country", how="inner")
# Merge with recovery rate
merged = pd.merge(
    recovery_rate, merged, on="Country", how="inner")
# Remove country column to produce correlation matrix
merged.drop(columns=["Country"], inplace=True)
# maintain type consistency produce correlation matrix
merged = merged.astype("float64")

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
columns = merged.columns
for i in range(2):
    for j in range(2):
        axes[i][j].scatter(merged[columns[j+2]], merged[columns[i]], s=15)
        # Reshape it to 2D array (required b4 fitting model)
        x = np.array(merged[columns[j+2]].values).reshape(-1, 1)
        # doesnt have to be 2D
        y = np.array(merged[columns[i]])
        # fitting model
        model = LinearRegression().fit(x, y)
        # plotting regression line
        axes[i][j].plot(x, model.predict(x), "-k",
                        label=f"R sq: {model.score(x, y):.2f}")
        # Set x and y labels
        axes[i][j].set(
            xlabel=f"{columns[j+2]}", ylabel=f"{columns[i]} (%)")
        # add % sign on y ticks
        axes[i][j].yaxis.set_major_formatter(
            mtick.PercentFormatter(decimals=0))
        axes[i][j].set_title(f"{columns[i]} vs {columns[j+2]}")
        axes[i][j].legend(loc="upper left", handlelength=0.3,
                          handletextpad=0.3)
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        axes[i][j].label_outer()

# Set global title
fig.suptitle(
    "Recovery rate and death rate vs Human Development Index and Life Expectancy per country")
plt.show()

# Create heatmap of the correlation matrix
plt.figure(figsize=(9, 6))

ax = sns.heatmap(merged.corr().iloc[:2, 2:], cmap=sns.color_palette("RdBu_r", 200), vmin=-
                 0.1, vmax=0.2, center=0, square=True, annot=True)

# set y ticks to horizontal
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
ax.set_title(
    "Heatmap of correlation matrix between recovery rate, death rate and HDI, life expentacy")

plt.show()

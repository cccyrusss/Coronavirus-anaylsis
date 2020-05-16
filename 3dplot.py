import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from util import country_vs_date
import matplotlib.cm as cm

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)

# Get confirmed cases of countries with top 10 number of confirmed cases
confirmed_cases = confirmed.drop(columns=["Total"]).sort_values(
    confirmed.last_valid_index(), axis=1, ascending=False).iloc[:, :10]

# Manual set up colour map with 10 different colours
colours = cm.jet(np.linspace(0, 1, 10))
for i in range(10):
    x, y = np.meshgrid(np.arange(i, i+2),
                       np.arange(len(confirmed_cases.index)))
    values = confirmed_cases.iloc[:, i:i+1].values
    np.append(values, values)
    ax.plot_surface(x, y, values,
                    rstride=1, cstride=1, color=colours[i], linewidth=0.5, edgecolor="black")
# Set xticks and yticks
ax.set_xticks(np.arange(len(confirmed_cases.columns)))
ax.set_xticklabels(confirmed_cases.columns, rotation=-90)
ax.set_yticks(np.arange(len(confirmed.index), step=10))
ax.set_yticklabels(confirmed.index[::10], rotation=-90)
# Set labels
ax.set_xlabel("Country")
ax.set_ylabel("Date")
ax.set_zlabel("Number of confirmed cases")
# Pad zticks
ax.tick_params(axis='z', which='major', pad=10)
# Pad labels
ax.xaxis.labelpad = 25
ax.yaxis.labelpad = 25
ax.zaxis.labelpad = 20

plt.title(
    "Time series ribbon plot of top 10 countries with the largest number of confirmed cases")
plt.show()

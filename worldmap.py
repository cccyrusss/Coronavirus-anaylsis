from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import matplotlib.pyplot as plt

confirmed_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
                           delimiter=',', skiprows=0, low_memory=False)
deaths_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
                        delimiter=',', skiprows=0, low_memory=False)
recovered_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
                           delimiter=',', skiprows=0, low_memory=False)

# Set up geometry
geometry = [Point(xy) for xy in zip(confirmed_df.Long, confirmed_df.Lat)]
geometry_d = [Point(xy) for xy in zip(deaths_df.Long, confirmed_df.Lat)]
geometry_r = [Point(xy) for xy in zip(recovered_df.Long, confirmed_df.Lat)]
# Set up geodataframes
gdf = GeoDataFrame(confirmed_df, geometry=geometry)
gdf_d = GeoDataFrame(deaths_df, geometry=geometry_d)
gdf_r = GeoDataFrame(recovered_df, geometry=geometry_r)


world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, alpha=0.4, color="grey", legend=True)
# Scales down marksize by 150 times
gdf.plot(ax=ax, alpha=0.5, legend=True, color="red", markersize=(
    confirmed_df.iloc[:, -2].values.real/150).astype(int))  # original last column, -2 because gdf added one at the end
gdf_d.plot(ax=ax, alpha=0.5, legend=True, color="blue", markersize=(
    deaths_df.iloc[:, -2].values.real/150).astype(int))  # original last column, -2 because gdf added one at the end
gdf_r.plot(ax=ax, alpha=0.5, legend=True, color="green", markersize=(
    recovered_df.iloc[:, -2].values.real/150).astype(int))  # original last column, -2 because gdf added one at the end

# Set up legends
ax.scatter([0], [0], c='red', alpha=0.5, s=50,
           label='Confirmed', edgecolor='red')
ax.scatter([0], [0], c='blue', alpha=0.5, s=50,
           label='Deaths', edgecolor='blue')
ax.scatter([0], [0], c='green', alpha=0.5, s=50,
           label='Recovered', edgecolor='green')
ax.legend(scatterpoints=1, frameon=True,
          labelspacing=0.6, loc='lower left', fontsize=10,
          bbox_to_anchor=(0.01, 0.01), title_fontsize=10)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title(
    "Bubble plot of the number of confirmed cases, deaths and people recovered at each location")
plt.show()

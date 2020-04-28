from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd 
import matplotlib.pyplot as plt

confirmed_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", delimiter=',', skiprows=0, low_memory=False)
deaths_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", delimiter=',', skiprows=0, low_memory=False)
recovered_df = pd.read_csv("data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(confirmed_df.Long, confirmed_df.Lat)]
geometry2 = [Point(xy) for xy in zip(deaths_df.Long, confirmed_df.Lat)]
geometry3= [Point(xy) for xy in zip(recovered_df.Long, confirmed_df.Lat)]
gdf = GeoDataFrame(confirmed_df, geometry=geometry)
gdf2 = GeoDataFrame(deaths_df, geometry=geometry2)
gdf3 = GeoDataFrame(recovered_df, geometry=geometry3)


world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, alpha=0.4, color="grey")
gdf.plot(ax=ax, alpha=0.5, legend=True, color="red", markersize=(confirmed_df.iloc[:, -2].values.real/50).astype(int)) # original last column, -2 because gdf added one at the end
gdf2.plot(ax=ax, alpha=0.5, legend=True, color="blue", markersize=(deaths_df.iloc[:, -2].values.real/50).astype(int)) # original last column, -2 because gdf added one at the end
gdf3.plot(ax=ax, alpha=0.5, legend=True, color="green", markersize=(recovered_df.iloc[:, -2].values.real/50).astype(int)) # original last column, -2 because gdf added one at the end
plt.show()


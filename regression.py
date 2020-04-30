import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from main import convert

# confirmed = convert(pd.read_csv(
#     "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"))
df = pd.read_excel(
    "data/Human Development Index/hdro_statistical_data_tables_1_15_d1_d5.xlsx", header=5, usecols="A:C")
df = df.drop(index=[0, 1])
df = df.rename({"(index value)": "HDI"}, axis=1)
df.set_index("HDI rank", inplace=True)
# df.iloc[0, 1] = "Human Development Index (HDI)"
print(df.head())

import matplotlib.pyplot as plt
import pandas as pd
from util import country_vs_date, plot

confirmed = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed = country_vs_date(confirmed)
confirmed_sorted = confirmed.sort_values(
    confirmed.last_valid_index(), axis=1, ascending=False)
# top 10 including "Total"
confirmed_top_10 = confirmed_sorted.iloc[:, :12]
# Total confirmed cases
plot(confirmed_top_10.loc[:, "Total"], "Time series of total confirmed cases",
     "Dates", "Number of confirmed cases")
# Confirmed cases except total
plot(confirmed_top_10.drop(columns=[
     "Total"]), "Time series of confirmed cases amongst countries", "Dates", "Number of confirmed cases")
# # bar chart of confirmed cases amongst countries (top 20)
# bar_plot(confirmed.iloc[:, :20].drop(columns=["Total"]).tail(1).T)

deaths = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
deaths = country_vs_date(deaths)
deaths_sorted = deaths.sort_values(
    deaths.last_valid_index(), axis=1, ascending=False)
plot(deaths_sorted.iloc[:, :11], "Time series of deaths",
     "Dates", "Number of deaths")

recovered = pd.read_csv(
    "data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
recovered = country_vs_date(recovered)
recovered_sorted = recovered.sort_values(
    recovered.last_valid_index(), axis=1, ascending=False)
plot(recovered_sorted.iloc[:, :11], "Time series of recovered",
     "Dates", "Number of recovered")
# death_rate = (deaths*100).div(confirmed).fillna(0)
# death_rate_sorted = death_rate.sort_values(
#     death_rate.last_valid_index(), axis=1, ascending=False)
# bar_plot(death_rate_sorted.iloc[:, :20].tail(1).T)

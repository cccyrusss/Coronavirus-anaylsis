# Convert time-series dataframe to a specific format (Country vs date)
def country_vs_date(df):
    df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
    df = df.groupby("Country/Region").sum()
    df.loc["Total"] = df.sum()
    return df.T

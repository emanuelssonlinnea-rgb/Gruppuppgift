# filen till nyckeltals-funktioner:

# Total intäkt 
# Totalt antal enheter
# AOV (Average Order Value)
# Intäkt per kategori
# Intäkt per stad
# Top-3 kategorier efter intäkt

import pandas as pd

#-----------BERÄKNINGAR AOV--------------
def calculate_aov(path="Gruppuppgift/data/clean_data.csv"):
    df = pd.read_csv(path)

# Konverting order date to a datetime type
    df["date"] = pd.to_datetime(df["date"])

# Adding column for month
    df["month"] = df["date"].dt.to_period("M").astype(str)

# Calculating total and monthly AOV
    total_aov = df["revenue"].sum() / df["order_id"].nunique()
    monthly_aov = (df.groupby("month")
                   .apply(lambda x: x["revenue"].sum() / x["order_id"].nunique())
                   .reset_index(name="AOV")
                      )
# Round & sort
    monthly_aov["AOV"] = monthly_aov["AOV"].round(0).astype(int)
    monthly_aov = monthly_aov.sort_values("month")
    return monthly_aov, round(total_aov)


# Intäkt per stad
df = pd.read_csv("Gruppuppgift/data/clean_data.csv")

revenue_per_city = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
df_revenue_city = revenue_per_city.reset_index()
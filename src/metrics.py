import pandas as pd

# Intäkt per stad
df = pd.read_csv("../Gruppuppgift/data/clean_data.csv")

revenue_per_city = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
df_revenue_city = revenue_per_city.reset_index()
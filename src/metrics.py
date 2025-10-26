# filen till nyckeltals-funktioner:

# Total intäkt 
# Totalt antal enheter
# AOV (Average Order Value)
# Intäkt per kategori
# Intäkt per stad
# Top-3 kategorier efter intäkt

import pandas as pd

# Read the data
df = pd.read_csv("../data/clean_data.csv")

# Calculating total AOV for the period
total_aov = df["revenue"].sum() / df["order_id"].count()
total_aov_rounded = round(total_aov)

# Checking order date is actually a datetime type
df["date"] = pd.to_datetime(df["date"])

# Extracting month to get AOV per month
df["month"] = df["date"].dt.to_period("M")

# Group by month and calculate AOV, round to whole number
monthly_aov = (df.groupby("month")
               .apply(lambda x: x["revenue"].sum() / x["order_id"].count())
                      .reset_index(name="AOV")
                      )

monthly_aov_rounded = round(monthly_aov)

# Sorting by month
monthly_aov_rounded = monthly_aov_rounded.sort_values("month")

print("Total AOV in the period:", total_aov_rounded)
print(monthly_aov_rounded)
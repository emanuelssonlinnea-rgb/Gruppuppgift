import pandas as pd

df = pd.read_csv("../Gruppuppgift/data/ecommerce_sales.csv")

# Quick check
# print(df.head())
# print(df.shape)
# print(df.dtypes)
# print(df.info())
# print(df.describe())

# Creating a copy to work on
df_clean = df.copy()

# Removing white space from columns and normalizing them
df_clean.columns = (df_clean.columns
                    .str.strip()
                    .str.replace(" ", "_")
                    .str.lower())

# None policy
print(df_clean.isna().sum()) 
# 0 none values, but if there were any, how would we manage them?
# order_id  - ignore
# date      - ignore
# city      - ignore
# category  - ignore
# price     - fill with the median
# units     - fill with the median
# revenue   - fill with the median

# Checking for duplicates in the id column
df_clean["order_id"].duplicated().sum()
# There are none but just in case:
df_clean["order_id"].drop_duplicates().reset_index(drop=True)

# Converting data type of some columns for efficency
df_clean[["order_id", "city", "category"]] = df_clean[["order_id", "city", "category"]].astype("category")
df_clean["date"] = pd.to_datetime(df_clean["date"])
#print(df_clean.dtypes)

# Sorting chronologically (to see if there are any odd dates)
df_clean = df_clean.sort_values(by="date")

# Saving the cleaned data in a new .csv
df_clean.to_csv("../Gruppuppgift/data/clean_data.csv", index = False)

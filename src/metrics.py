# Intäkter per kategori

# Kräver att man först öppnar en csv och därefter kör "variabel" = csvreader, och matar sedan in variabeln i revenue_per_category(reader)
import csv
import numpy as np
import matplotlib as plt

def revenue_per_category(reader): 
    dictionary_of_category_and_revenue = {}
    list_of_category_and_revenue = []
    next(reader)

    for row in reader:
        if row[3] not in dictionary_of_category_and_revenue:
            dictionary_of_category_and_revenue[row[3]] = float(row[6])
        elif row[3] in dictionary_of_category_and_revenue:
            dictionary_of_category_and_revenue[row[3]] += float(row[6])
        else:
            print("Error - cannot read your input variabel correctly. Please check if it is a dictionary! Only dictionaries here plz <3")

    for category, revenue in dictionary_of_category_and_revenue.items():
        list_of_category_and_revenue.append((category, revenue))
    
    return sorted(list_of_category_and_revenue, key=lambda item: item[1], reverse=True)
    

# filen till nyckeltals-funktioner:

# Total intäkt 
# Totalt antal enheter
# AOV (Average Order Value)
# Intäkt per kategori
# Intäkt per stad
# Top-3 kategorier efter intäkt

import pandas as pd

#-----------BERÄKNINGAR AOV--------------
def calculate_aov(path="data/clean_data.csv"):
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
def revenue_per_city(path="data/clean_data.csv"):
    df = pd.read_csv(path)

    revenue_per_city = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
    df_revenue_city = revenue_per_city.reset_index()

    return df_revenue_city
import pandas as pd
from metrics import total_units_sold

# Beräknar totalt antal enheter sålda
def total_units_sold(df):
    # Summerar alla värden i kolumnen 'quantity'
    total_units = df["quantity"].sum()
    # Returnerar resultatet
    return total_units



# Laddar in datan (om den inte redan är laddad)
df = pd.read_csv("data/clean_data.csv")

# Anropar funktionen
total = total_units_sold(df)

print("Totalt antal enheter sålda:", total)

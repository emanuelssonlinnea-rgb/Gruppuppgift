# filen till plot-funktioner
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import matplotlib.pyplot as plt

from metrics import df_revenue_city 

# Scaling to thousands for readability purposes
df_revenue_city["revenue_thousands"] = df_revenue_city["revenue"] / 1000

# Bar chart to show revenue per city
fig, ax = plt.subplots()
ax.bar(df_revenue_city["city"], df_revenue_city["revenue_thousands"], color="LightGreen")
ax.set_title("Total revenue per city")
ax.set_xlabel ("City")
ax.set_ylabel("Revenue (thousands)")
ax.grid(True, axis="y")
plt.tight_layout()
plt.show()
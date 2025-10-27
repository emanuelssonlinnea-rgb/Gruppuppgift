# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import matplotlib.pyplot as plt

#------------PLOTTING AOV--------------

# hämtar datan från beräkningsfilen
from metrics import calculate_aov 
monthly_aov, total_aov = calculate_aov()

# Skapar ett stapeldiagram
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(monthly_aov["month"], monthly_aov["AOV"], color="blue")
ax.axhline(y=total_aov, color="orange", linestyle="--")

# lägger till etiketter (AOV värdena) ovanför stolparna
for i, v in enumerate(monthly_aov["AOV"]):
    ax.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

# anpassar utseendet
ax.set_title("Genomsnittlig orderstorlek (AOV) per månad")
ax.set_xlabel("Månad")
ax.set_ylabel("AOV i kr")
ax.set_ylim(400, 2000)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
#________________________________________

# --- Intäkt per stad ---
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
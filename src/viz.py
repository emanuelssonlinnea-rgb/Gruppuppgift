# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import matplotlib.pyplot as plt

#------------AOV--------------

# hämtar datan från beräkningsfilen
from metrics import calculate_aov
monthly_aov, total_aov, category_aov = calculate_aov()

# AOV - ÖVER TID - STAPELDIAGRAM 
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(monthly_aov["month"], monthly_aov["AOV"], color="orange")
ax.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label=" Genomsnittlig AOV i perioden")

# lägger till etiketter (AOV värdena) på stolparna 
for i, v in enumerate(monthly_aov["AOV"]):
    ax.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

# anpassar utseendet
ax.set_title("Genomsnittlig orderstorlek (AOV) per månad")
ax.set_xlabel("Månad")
ax.set_ylabel("AOV i kr")
ax.set_ylim(0, 2000)
ax.grid(True, axis="y")
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# AOV - KATEGORI - STAPELDIAGRAM
fig, ax = plt.subplots(figsize=(10, 6))
plt.bar(category_aov["category"], category_aov["AOV"], color="seagreen")
ax.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="Genomsnittlig AOV")

for i, v in enumerate(category_aov["AOV"]):
    ax.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

ax.set_title("Genomsnittlig orderstorlek (AOV) per kategori")
ax.set_xlabel("Kategori")
ax.set_ylabel("AOV i kr")
ax.set_ylim(0, 3000)
ax.grid(True, axis="y")
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

#________________________________________

# --- Intäkt per stad ---
from src.metrics import revenue_per_city

def plot_tot_revenue_per_city(df):
    """
    Plots the total revenue per city in a bar chart
    """

    # Calculate the metric
    df_revenue_city = revenue_per_city(df)

    # Scaling to thousands for readability purposes
    df_revenue_city["revenue_thousands"] = df_revenue_city["total_revenue"] / 1000

    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(
        df_revenue_city["city"], 
        df_revenue_city["revenue_thousands"], 
        color="LightGreen"
    )
    
    ax.set_title("Total revenue per City")
    ax.set_xlabel ("City")
    ax.set_ylabel("Revenue (thousands)")
    ax.grid(True, axis="y", alpha=0.5)

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
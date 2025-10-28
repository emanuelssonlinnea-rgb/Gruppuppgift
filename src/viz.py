# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import matplotlib.pyplot as plt

#------------AOV I EN FIGUR--------------

# hämtar datan från beräkningsfilen
from metrics import calculate_aov

def plot_aov_figure(df):
    monthly_aov, total_aov, category_aov, city_aov = calculate_aov()

    # Skapar en figur med tre deldigram bredvid varandra
    fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharex=False, sharey=False)

    # Delgraf 1: AOV over time
    ax1 = axes[0]
    ax1.bar(monthly_aov["month"], monthly_aov["AOV"], color="orange")
    ax1.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="Genomsnittlig AOV")

    # lägger till etiketter (AOV värdena) på stolparna 
    for i, v in enumerate(monthly_aov["AOV"]):
        ax1.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    # anpassar utseendet
    ax1.set_title("AOV per månad")
    ax1.set_xlabel("Månad")
    ax1.set_ylabel("AOV i kr")
    ax1.set_ylim(0, 2300)
    ax1.grid(True, axis="y")
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    # Delgraf 2: AOV per kategori
    ax2 = axes[1]
    ax2.bar(category_aov["category"], category_aov["AOV"], color="seagreen")
    ax2.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="Genomsnittlig AOV")

    for i, v in enumerate(category_aov["AOV"]):
        ax2.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax2.set_title("AOV per kategori")
    ax2.set_xlabel("Kategori")
    ax2.set_ylabel("AOV i kr")
    ax2.set_ylim(0, 2300)
    ax2.grid(True, axis="y")
    ax2.legend()
    ax2.tick_params(axis='x', rotation=45)

    # Delgraf 3: AOV per stad
    ax3 = axes[2]
    ax3.bar(city_aov["city"], city_aov["AOV"], color="blue")
    ax3.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="Genomsnittlig AOV")

    for i, v in enumerate(city_aov["AOV"]):
        ax3.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax3.set_title("AOV per kategori")
    ax3.set_xlabel("Kategori")
    ax3.set_ylabel("AOV i kr")
    ax3.set_ylim(0, 2300)
    ax3.grid(True, axis="y")
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    # Gemensam titel
    fig.suptitle("Genomsnittlig orderstorlek (AOV) – Översikt", fontsize=16, fontweight="bold")

    plt.tight_layout()
    plt.show()


# --- Intäkt per stad ---
#from src.metrics import revenue_per_city
from metrics import revenue_per_city
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
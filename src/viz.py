# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import pandas as pd
import matplotlib.pyplot as plt

#------------PLOTTING ALL AOV I ONE FIGURE------------------

def plot_aov_figure(monthly_aov: pd.DataFrame, total_aov: pd.DataFrame, category_aov: pd.DataFrame, city_aov: pd.DataFrame):
    # Skapar en figur med tre deldigram bredvid varandra
    fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharex=False, sharey=False)

    # Delgraf 1: AOV over time
    ax1 = axes[0]
    ax1.bar(monthly_aov["month"], monthly_aov["AOV"], color="orange")
    ax1.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    # lägger till etiketter (AOV värdena) på stolparna 
    for i, v in enumerate(monthly_aov["AOV"]):
        ax1.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    # anpassar utseendet
    ax1.set_title("AOV per month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("AOV in kr")
    ax1.set_ylim(0, 2300)
    ax1.grid(True, axis="y")
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    # Delgraf 2: AOV per kategori
    ax2 = axes[1]
    ax2.bar(category_aov["category"], category_aov["AOV"], color="seagreen")
    ax2.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    for i, v in enumerate(category_aov["AOV"]):
        ax2.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax2.set_title("AOV per category")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("AOV in kr")
    ax2.set_ylim(0, 2300)
    ax2.grid(True, axis="y")
    ax2.legend()
    ax2.tick_params(axis='x', rotation=45)

    # Delgraf 3: AOV per stad
    ax3 = axes[2]
    ax3.bar(city_aov["city"], city_aov["AOV"], color="blue")
    ax3.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    for i, v in enumerate(city_aov["AOV"]):
        ax3.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax3.set_title("AOV per city")
    ax3.set_xlabel("City")
    ax3.set_ylabel("AOV in kr")
    ax3.set_ylim(0, 2300)
    ax3.grid(True, axis="y")
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    # Gemensam titel
    fig.suptitle("Average Order Value (AOV) – Overview", fontsize=16, fontweight="bold")

    plt.tight_layout()
    plt.show()



# --- Total Intäkt & Intäkt över tid (månad) ---
# hämtar datan från beräkningsfilen

#from src.metrics import revenue_over_time, total_revenue 
#calculate_revenue = revenue_over_time, total_revenue



def revenue_monthly_bar(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    fig, ax = plt.subplots(figsize=(9,4))
    ax.set_title("Revenue per month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.grid(grid, axis = "y")
    ax.legend()

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    return ax


    



import matplotlib.pyplot as plt
import pandas as pd
from src import *

#------------AOV I EN FIGUR--------------

# hämtar datan från beräkningsfilen
# from src.metrics import calculate_aov 
# monthly_aov, total_aov = calculate_aov()
# from metrics import *

def plot_aov_figure(df: pd.DataFrame):
    monthly_aov, total_aov, category_aov, city_aov = calculate_aov(df)

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

# Function for bar plots
def bar(ax, x, y, title, xlabel, ylabel, color, grid: bool = True):
    ax.bar(x, y, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y", alpha=0.5)
    plt.xticks(rotation=45)
    return ax
# --- Total Intäkt & Intäkt över tid (månad) ---
# hämtar datan från beräkningsfilen


# calculate_revenue = metrics.revenue_over_time, metrics.total_revenue



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


# Jakobs 

def plot_revenue_per_category(df1: pd.DataFrame, df2: pd.DataFrame):
    fig, axes = plt.subplots(1,2, figsize=(10,8))
    df1.plot(kind="bar", ax=axes[0], legend=False)
    axes[0].set_title("Revenue per category")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Revenue in thousands")
    axes[0].tick_params(axis='x', rotation=0)

    df2.plot(kind="bar", ax=axes[1], legend=False)
    axes[1].set_title("Top 3 revenue per month")
    axes[1].tick_params(axis='x', rotation=0)
    fig.suptitle("Revenue per category and top 3 revenue per category", y=1.02)

    plt.tight_layout()
    plt.show()

def boxplot_revenue_per_category(df: pd.DataFrame) -> pd.DataFrame:
    fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="category", ax=ax)
    ax.set_title("Revenue per category")
    ax.set_xlabel("")
    ax.set_ylabel("Revenue per thousands")
    plt.suptitle("")
    plt.tight_layout()
    plt.show()


    



# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.metrics import *

from src import * 
"""
from src import * imports all the functions from all the files in the folder src. After this import we don't need any other.
"""

#------------PLOTTING ORDER VALUE IN ONE FIGURE------------------

def plot_ov_figure(monthly_aov: pd.DataFrame, total_aov: float, category_aov: pd.DataFrame, city_aov: pd.DataFrame, ave_units_per_order: float, df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(16, 16), sharex=False, sharey=False)

    # Delgraf 1: AOV over time
    ax1 = axes[0, 0]
    ax1.bar(monthly_aov["month"], monthly_aov["AOV"], color="orange")
    ax1.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")
    
    # lägger till etiketter (AOV värdena) på stolparna 
    for i, v in enumerate(monthly_aov["AOV"]):
        ax1.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    # anpassar utseendet
    ax1.set_title("Average Order Value (AOV) per month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("AOV (kr)")
    ax1.set_ylim(0, 2300)
    ax1.grid(True, axis="y")
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    # Delgraf 2: AOV per kategori
    ax2 = axes[0, 1]
    ax2.bar(category_aov["category"], category_aov["AOV"], color="seagreen")
    ax2.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    for i, v in enumerate(category_aov["AOV"]):
        ax2.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax2.set_title("Average Order Value (AOV) per category")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("AOV (kr)")
    ax2.set_ylim(0, 2300)
    ax2.grid(True, axis="y")
    ax2.legend()
    ax2.tick_params(axis='x', rotation=45)

    # Delgraf 3: Units sold per category
    ax3 = axes[1, 0]
    # Grupperar units per kategori
    groups = df.groupby("category")["units"]
    # Skapar en litsa med units-värden för varje kategori
    units_data = [group.values for name, group in groups]
    # Skapar en lista med kategorinamnen (etiketter)
    labels = [name for name, group in groups]
    # Ritar boxploten
    ax3.boxplot(units_data, labels=labels, vert=True, patch_artist=True)
    # Lägger till referenslinje och 
    ax3.axhline(y=ave_units_per_order, color="grey", linestyle="--", linewidth=1, label="Average units per order")

    ax3.set_title("Distribution of sold units per catgeory")
    ax3.set_xlabel("Category")
    ax3.set_ylabel("Number of units")
    ax3.set_ylim(0, 10)
    ax3.grid(True, axis="y")
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    # AOV per city 
    #ax3.bar(city_aov["city"], city_aov["AOV"], color="blue")
    #ax3.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    #for i, v in enumerate(city_aov["AOV"]):
        #ax3.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    #ax3.set_title("AOV per city")
    #ax3.set_xlabel("City")
    #ax3.set_ylabel("AOV in kr")
    #ax3.set_ylim(0, 2300)
    #ax3.grid(True, axis="y")
    #ax3.legend()
    #ax3.tick_params(axis='x', rotation=45)

     # Delgraf 4: Ordervalue per category
    ax4 = axes[1, 1]
    # Grupperar revenue per kategori
    groups = df.groupby("category")["revenue"]
    # Skapar en litsa med revenue-värden för varje categori
    rev_data = [group.values for name, group in groups]
    # Skapar en lista med kategorinamnen (etiketter)
    labels = [name for name, group in groups]
    # Ritar boxploten
    ax4.boxplot(rev_data, labels=labels, vert=True, patch_artist=True)
    # Lägger till referenslinje och 
    ax4.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")

    ax4.set_title("Distribution of Order Value per catgeory")
    ax4.set_xlabel("Category")
    ax4.set_ylabel("Revenue in kr")
    ax4.set_ylim(0, 10000)
    ax4.grid(True, axis="y")
    ax4.legend()
    ax4.tick_params(axis='x', rotation=45)

    # Gemensam titel
    fig.suptitle("Order Value – Overview", fontsize=16, fontweight="bold")

    plt.tight_layout()
    plt.show()



# --- Total Intäkt & Intäkt över tid (månad) ---

def revenue_monthly_bar(df: pd.DataFrame) -> pd.DataFrame:
    fig, ax = plt.subplots(figsize=(9,4))
    # ax.bar(sumclass["month"], sumclass["revenue"], color="skyblue", edgecolor="black")
    # ax.set_title("Revenue per month")
    # ax.set_xlabel("Month")
    # ax.set_ylabel("Revenue")
    # ax.grid(True, axis = "y")
    # ax.legend()
    # plt.xticks(rotation=45, ha="right")
    # plt.tight_layout()
    # plt.show()



    ax.hist(df["month"] , bins=12, color="skyblue", edgecolor="black")
    ax.set_title("Revenue per month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis = "y")
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

  
def revenue_monthly_boxplot(df: pd.DataFrame) -> pd.DataFrame:
    fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="month", ax=ax)
    ax.set_title("Revenue per month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    plt.suptitle("")
    plt.tight_layout()
    plt.show()


# -- Intäkt per kategori --
# Plottar intäkt per kategori samt top 3 kategorier och plot med outliers

def plot_revenue_per_category(df1: pd.DataFrame):
    df_revenue_per_category_1 = revenue_per_category(df1)
    df_top_3_revenue_per_category = top_3_revenue_per_category(df1)
    fig, axes = plt.subplots(1,2, figsize=(10,8))
    df_revenue_per_category_1.plot(kind="bar", ax=axes[0], legend=False)
    axes[0].set_title("Revenue per category")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Revenue in thousands")
    axes[0].tick_params(axis='x', rotation=0)

    df_top_3_revenue_per_category.plot(kind="bar", ax=axes[1], legend=False)
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
    ax.set_ylabel("Revenue")
    plt.suptitle("")
    plt.tight_layout()
    plt.show()


# Funktion till bar plot
def bar(ax, x, y, title, xlabel, ylabel, color, grid: bool = True):
    ax.bar(x, y, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y", alpha=0.5)
    plt.xticks(rotation=45)
    return ax




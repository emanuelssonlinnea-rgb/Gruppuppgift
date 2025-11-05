import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.metrics import *

#------------PLOTTING ORDER VALUE IN ONE FIGURE------------------

def plot_aov_figure(monthly_aov: pd.DataFrame, total_aov: float, category_aov: pd.DataFrame):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharex=False, sharey=False)

    # Delgraf 1: Montly AOV
    ax1 = axes[0]
    ax1.bar(monthly_aov["month"], monthly_aov["AOV"], color="orange")
    ax1.axhline(y=total_aov, color="grey", linestyle="--", linewidth=1, label="AOV all orders")
    
    for i, v in enumerate(monthly_aov["AOV"]):
        ax1.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

    ax1.set_title("Average Order Value (AOV) per month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("AOV (kr)")
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

    ax2.set_title("Average Order Value (AOV) per category")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("AOV (kr)")
    ax2.set_ylim(0, 2300)
    ax2.grid(True, axis="y")
    ax2.legend()
    ax2.tick_params(axis='x', rotation=45)

    fig.suptitle("Average Order Value – Overview", fontsize=16, fontweight="bold")

    plt.tight_layout()
    plt.show()

#------------BOX PLOT UNITS SOLD PER CATEGORY------------------

def box_plot_units_per_category (ave_units_per_order: float, df: pd.DataFrame):
  
    groups = df.groupby("category")["units"]
    units_data = [group.values for name, group in groups]
    labels = [name for name, group in groups]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(units_data, labels=labels, vert=True, patch_artist=True)
    ax.axhline(y=ave_units_per_order, color="grey", linestyle="--", linewidth=1, label="Average units per order")

    ax.set_title("Distribution of sold units per catgeory")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of units")
    ax.set_ylim(0, 10)
    ax.grid(True, axis="y")
    ax.legend()
    ax.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

# --- Total Intäkt & Intäkt över tid (månad) ---

def revenue_monthly_bar(monthly_revenue: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9,4))
    ax.hist(monthly_revenue["revenue"] , bins=30, color="skyblue", edgecolor="black")
    ax.set_title("Revenue per month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis = "y")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# def revenue_monthly_hist(df: pd.DataFrame) -> pd.DataFrame:
#     fig, ax = plt.subplots(figsize=(9,4))
#     ax.hist(df["month"] , bins=12, color="skyblue", edgecolor="black")
#     ax.set_title("Revenue per month")
#     ax.set_xlabel("Month")
#     ax.set_ylabel("Revenue")
#     ax.grid(True, axis = "y")
#     plt.xticks(rotation=45, ha="right")
#     plt.tight_layout()
#     plt.show()


  
def revenue_monthly_boxplot(df: pd.DataFrame) -> pd.DataFrame:
    fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="month", ax=ax)
    ax.set_title("Revenue per month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
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
    axes[0].tick_params(axis="x", rotation=0)
    

    df_top_3_revenue_per_category.plot(kind="bar", ax=axes[1], legend=False)
    axes[1].set_title("Top 3 revenue per month")
    axes[1].tick_params(axis="x", rotation=0)
    fig.suptitle("Revenue per category and top 3 revenue per category", y=1.02)

    plt.tight_layout()
    plt.show()


def boxplot_revenue_per_category(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="category", ax=ax)
    ax.set_title("Revenue per category")
    ax.set_xlabel("")
    ax.set_ylabel("Revenue")
    ax.axhline(y=calculate_total_aov(df), color="grey", linestyle="--", linewidth=1, label="AOV all orders")
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




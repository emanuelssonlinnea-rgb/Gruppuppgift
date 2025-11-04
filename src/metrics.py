# # Intäkter per kategori

# # Kräver att man först öppnar en csv och därefter kör "variabel" = csvreader, och matar sedan in variabeln i revenue_per_category(reader)
# import csv
import pandas as pd

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
    
#-----------BERÄKNINGAR AOV--------------

# Laddar och förbereder datan
def load_and_prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df

# Beräknar AOV för samtliga ordrar 
def calculate_total_aov(df: pd.DataFrame) -> pd.DataFrame:
    total_aov = df["revenue"].sum() / df["order_id"].nunique()
    return total_aov

# Beräkning av AOV över tid (totalt & månad)
def calculate_aov_per_month(df: pd.DataFrame) -> pd.DataFrame:
    monthly_aov = (df.groupby("month")
                   .apply(lambda x: x["revenue"].sum() / x["order_id"].nunique())
                   .reset_index(name="AOV")
                      )
    # Rundar & sorterar
    monthly_aov["AOV"] = monthly_aov["AOV"].round(0).astype(int)
    monthly_aov = monthly_aov.sort_values("month")
    return monthly_aov

# Beräkning av AOV per kategori
def calculate_aov_per_category(df: pd.DataFrame) -> pd.DataFrame:
    category_aov = (df.groupby("category")
                    .apply(lambda x: x["revenue"].sum() / x["order_id"].nunique())
                    .reset_index(name="AOV")
                    )
    category_aov["AOV"] = category_aov["AOV"].round(0).astype(int)
    return category_aov

# Huvudfunktion som kör allt
def calculate_aov(df: pd.DataFrame) -> tuple[pd.DataFrame, float, pd.DataFrame, pd.DataFrame]:
    df = load_and_prepare_data(df)
    monthly_aov = calculate_aov_per_month(df)
    total_aov = calculate_total_aov(df)
    category_aov = calculate_aov_per_category(df)
    
    return monthly_aov, total_aov, category_aov

#------------Uträkningar för medel & spridning av sålda enheter per kategori-----------------------------
def calculate_average_units_per_order(df: pd.DataFrame) -> float:
    ave_units_per_order = df["units"].sum() / df["order_id"].count()
    return round(float(ave_units_per_order), 2)

def calculate_distribution_units_sold(df: pd.DataFrame) -> tuple[float, pd.DataFrame]:
    df = load_and_prepare_data(df)
    ave_units_per_order = calculate_average_units_per_order(df)
    return ave_units_per_order, df

#------------- Revenue per city---------------------------------------
def revenue_per_city(df: pd.DataFrame) -> pd.DataFrame:
    """
    Where do we sell?
    """
    return (
        df.groupby("city", observed=True)
        .agg(tot_rev_city=("revenue", "sum"))
        .sort_values("tot_rev_city", ascending=False)
        .reset_index())

# Top 3 cities
def top3_cities(df: pd.DataFrame) -> pd.DataFrame:
    return revenue_per_city(df).head(3)


#-----------BERÄKNINGAR TOTAL INTÄKT & INTÄKT ÖVER TID (MÅNAD)--------------

#df = pd.read_csv(r"c:\Users\Mauro\Desktop\Gruppuppgift -Linnéa branch\Gruppuppgift\data\clean_data.csv")


# Total Intäkt

def total_revenue(df: pd.DataFrame) -> pd.DataFrame:
    
    return int(df["revenue"].sum())


# Intäkt över tid (månad)

def revenue_over_time(df: pd.DataFrame, freq: str = "M") -> pd.DataFrame:
    """
    When do we get the highest vs smallest revenue?
    """
    ts = (
        df.set_index("month")
        .sort_index()
        .resample(freq)["revenue"]
        .nunique()
        .reset_index()
       )
    ts["month"] = ts["month"].dt.strftime("%Y-%m")   # Convert 'month' column to string format like '2024-01'
    
    return ts


# Revenue per category
def revenue_per_category(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby(["category"])["revenue"].sum() / 1000).sort_values(ascending=False)

def top_3_revenue_per_category(df: pd.DataFrame) -> pd.DataFrame:
    top_3_category = revenue_per_category(df).head(3)
    return top_3_category

# Lookout, there are outliers!
def looking_for_them_outliers_in_category_revenue(df: pd.DataFrame):
    category_revenue_grouped = df.groupby(["category"])["revenue"]
    number_of_them_outliers = {}
    outliers_revenue = {}
    revenue_without_outliers = {}

    for category, category_rows in category_revenue_grouped:
        Q1 = category_rows.quantile(0.25)
        Q3 = category_rows.quantile(0.75)
        IQR = Q3 - Q1

        low = Q1 - (1.5 * IQR)
        high = Q3 + (1.5 * IQR)
        
        outliers = category_rows[(category_rows < low) | (category_rows > high)]
        outliers_revenue[category] = outliers.sum()
        number_of_them_outliers[category] = len(outliers)

        revenue_without_outliers[category] = ((category_rows.sum()) - (outliers.sum()))


    return ((pd.Series(number_of_them_outliers).sort_values(ascending=False)), (pd.Series(outliers_revenue).sort_values(ascending=False))), (pd.Series(revenue_without_outliers).sort_values(ascending=False))





    



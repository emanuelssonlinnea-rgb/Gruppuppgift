import pandas as pd

REQUIRED = [
    "order_id","date","city","category","price","units","revenue"
]

def load_data(path: str) -> pd.DataFrame:
    """
    Loads the CSV file, checks that all the columns are present and returns a dataframe
    """
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing column: {missing}")
    return df

def fill_unknown(s: pd.Series, missing_label: str = "Unknown") -> pd.Series:
    """Replace missing values in a categorical column with a label"""
    return s.astype("object").fillna(missing_label)

def coerce_numeric(s: pd.Series) -> pd.Series:
    """Convert a Series to numeric, coercing errors and filling NaNs with 0"""
    return pd.to_numeric(s, errors="coerce").fillna(0)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and processes the e-commerce sales data.
    
    - Standardize column names
    - Handles missing values
    - Convert data types
    - Add month and week to columns
    """
    df_clean = df.copy()

    # Removing white space from columns and normalizing them
    df_clean.columns = (df_clean.columns
                        .str.strip()
                        .str.replace(" ", "_")
                        .str.lower()
    )

    # Dropping duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # Converting data type
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Fill categorical NaNs
    for col in ["order_id", "city", "category"]:
        df[col] = fill_unknown(df[col])
    
    # Convert to categorical
    for col in ["order_id", "city", "category"]:
        df[col] = df[col].astype("category")

    # Coerce numeric columns
    for col in ["price", "units", "revenue"]:
        df[col] = coerce_numeric(df[col])

    # Add derived time columns
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    df["week"] = df["date"].dt.to_period("W").dt.start_time

    # Sort by date
    df = df.sort_values(by="date")

    return df

def save_data(df: pd.DataFrame, path: str) -> None:
    """Save cleaned data to CSV"""
    df.to_csv(path, index=False)

import pandas as pd

# Open and read the file
def read_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

# Cleaning the dataframe
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Dropping duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # Converting the data column in datetype
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    # Coerce numeric colums and fill the Naans with 0
    for col in ["price", "units", "revenue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    
    return df
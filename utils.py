import pandas as pd


def load_data() -> pd.DataFrame:
    """Load the Titanic dataset into a pandas DataFrame."""
    return pd.read_csv("data/titanic.csv")

def filter_passengers(df):
    return df[df["sex"] == "male"]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a pandas DataFrame.

    This function drops rows that contain any missing values and converts
    all categorical (object/category) columns to lowercase strings.

    Parameters:
        df (pd.DataFrame): Input DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame with missing rows removed and
        categorical columns lowercased.
    """
    # Drop rows that have any missing values
    cleaned = df.dropna().copy()

    # Convert object/category columns to lowercase strings
    cat_cols = cleaned.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        cleaned[col] = cleaned[col].astype(str).str.lower()

    return cleaned

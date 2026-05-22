
def filter_males(df):
	"""Return rows where the sex column equals 'male'."""
	# If there is no 'sex' column return an empty dataframe with same columns
	if "sex" not in df.columns:
		return df.iloc[0:0]
	# Normalize values to string and compare case-insensitively
	sex_series = df["sex"].astype(str).str.lower()
	return df[sex_series == "male"]

import pandas as pd


def load_data() -> pd.DataFrame:
    """Load the Titanic dataset into a pandas DataFrame."""
    return pd.read_csv("data/titanic.csv")

def filter_passengers(df):
    return df[df["sex"] == "male"]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame with rows containing missing
    values dropped and categorical columns converted to lowercase.
    """
    # Drop rows with any missing values
    cleaned = df.dropna().copy()

    # Find categorical/object columns and convert their string values to lowercase
    cat_cols = cleaned.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        cleaned[col] = cleaned[col].astype(str).str.lower()

    return cleaned

import pandas as pd


def load_data() -> pd.DataFrame:
    """Load the Titanic dataset into a pandas DataFrame."""
    return pd.read_csv("data/titanic.csv")

def filter_passengers(df):
    return df[df["sex"] == "male"]

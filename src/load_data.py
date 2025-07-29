"""
load_data.py

Handles loading and basic inspection of the tweet dataset.
"""

import pandas as pd

def load_csv(filepath):
    """
    Loads a CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def preview_data(df, n=5):
    """
    Prints the first few rows of the DataFrame.
    """
    print(df.head(n))
    print("\nDataFrame Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

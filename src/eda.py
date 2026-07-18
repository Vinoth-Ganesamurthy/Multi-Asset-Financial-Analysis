"""
Module: eda.py

Purpose:
    Perform exploratory data analysis (EDA) on multiple financial assets.

Datasets:
    - Gold
    - Silver
    - S&P 500
    - Bitcoin

Author:
    Vinoth Ganesamurthy
"""

import pandas as pd

from config import (
    GOLD_FILE,
    SILVER_FILE,
    SP500_FILE,
    BITCOIN_FILE,
)

def load_market_data() -> dict:
    """
    Load all market datasets.
    """

    datasets = {
        "Gold": pd.read_csv(GOLD_FILE,  index_col=0),
        "Silver": pd.read_csv(SILVER_FILE, index_col=0),
        "S&P500": pd.read_csv(SP500_FILE, index_col=0),
        "Bitcoin": pd.read_csv(BITCOIN_FILE, index_col=0),
    }

    return datasets

def validate_market_data(datasets: dict) -> None:
    """
    Validate each dataset.

    Parameters
    ----------
    datasets : dict
        Dictionary containing all market datasets.
    """

    for asset, df in datasets.items():
        print("=" * 40)
        print(f"Asset: {asset}")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print(df.head())
if __name__ == "__main__":

    datasets = load_market_data()
    validate_market_data(datasets)
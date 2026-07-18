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
        "Gold": pd.read_csv(GOLD_FILE, index_col=0),
        "Silver": pd.read_csv(SILVER_FILE, index_col=0),
        "S&P500": pd.read_csv(SP500_FILE, index_col=0),
        "Bitcoin": pd.read_csv(BITCOIN_FILE, index_col=0),
    }

    return datasets


def validate_market_data(datasets: dict) -> None:
    """
    Validate each dataset.
    """

    for asset, df in datasets.items():

        print("=" * 40)
        print(f"Asset: {asset}")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print(df.head())
        print()


def descriptive_statistics(datasets: dict) -> pd.DataFrame:
    """
    Generate descriptive statistics for the Close price
    of each financial asset.
    """

    summary = []

    for asset, df in datasets.items():

        close = df["Close"]

        summary.append(
            {
                "Asset": asset,
                "Observations": close.count(),
                "Mean": close.mean(),
                "Median": close.median(),
                "Std Dev": close.std(),
                "Minimum": close.min(),
                "Maximum": close.max(),
            }
        )

    summary_df = pd.DataFrame(summary)

    print("\n" + "=" * 60)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 60)
    print(summary_df)

    return summary_df


if __name__ == "__main__":

    datasets = load_market_data()

    validate_market_data(datasets)

    descriptive_statistics(datasets)
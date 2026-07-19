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


def calculate_daily_returns(datasets: dict) -> dict:
    """
    Calculate daily percentage returns for each asset.
    """

    returns = {}

    for asset, df in datasets.items():

        returns_df = df.copy()

        returns_df["Daily Return"] = returns_df["Close"].pct_change()

        # Remove the first row containing NaN
        returns_df.dropna(inplace=True)

        returns[asset] = returns_df

    return returns

def average_daily_returns(returns: dict) -> None:
    """
    Display the average daily return for each asset.
    """

    print("\n" + "=" * 40)
    print("AVERAGE DAILY RETURNS")
    print("=" * 40)

    for asset, df in returns.items():

        avg_return = df["Daily Return"].mean()

        print(f"{asset:<10}: {avg_return:.6f}")

def volatility_analysis(returns: dict) -> None:
    """
    Display the daily volatility (standard deviation)
    of returns for each asset.
    """

    print("\n" + "=" * 40)
    print("DAILY VOLATILITY")
    print("=" * 40)

    for asset, df in returns.items():

        volatility = df["Daily Return"].std()

        print(f"{asset:<10}: {volatility:.6f}")

def correlation_analysis(returns: dict) -> pd.DataFrame:
    """
    Calculate the correlation matrix of daily returns.
    """

    correlation_df = pd.DataFrame()

    for asset, df in returns.items():

        correlation_df[asset] = df["Daily Return"]

    correlation_matrix = correlation_df.corr()

    print("\n" + "=" * 50)
    print("CORRELATION MATRIX")
    print("=" * 50)
    print(correlation_matrix)

    return correlation_matrix

if __name__ == "__main__":

    # Load datasets
    datasets = load_market_data()

    # Validate datasets
    validate_market_data(datasets)

    # Descriptive statistics
    descriptive_statistics(datasets)

    # Calculate daily returns
    returns = calculate_daily_returns(datasets)

    # Average daily returns
    average_daily_returns(returns)

    # Daily volatility
    volatility_analysis(returns)

    # Correlation analysis
    correlation_analysis(returns)
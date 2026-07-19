"""
Module: visualization.py

Purpose:
    Create visualizations for financial data.

Author:
    Vinoth Ganesamurthy
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

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
        "Gold": pd.read_csv(GOLD_FILE, index_col=0, parse_dates=True),
        "Silver": pd.read_csv(SILVER_FILE, index_col=0, parse_dates=True),
        "S&P500": pd.read_csv(SP500_FILE, index_col=0, parse_dates=True),
        "Bitcoin": pd.read_csv(BITCOIN_FILE, index_col=0, parse_dates=True),
    }

    for _, df in datasets.items():
        df.sort_index(inplace=True)

    return datasets


def plot_normalized_prices(datasets: dict) -> None:
    """
    Plot normalized closing prices (Base = 100).
    """

    plt.figure(figsize=(12, 6))

    for asset, df in datasets.items():

        normalized_price = (df["Close"] / df["Close"].iloc[0]) * 100

        plt.plot(df.index, normalized_price, linewidth=2, label=asset)

    plt.title("Normalized Asset Performance (Base = 100)")
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.yscale("log")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(datasets: dict) -> None:
    """
    Plot correlation heatmap of daily returns.
    """

    returns = pd.DataFrame()

    for asset, df in datasets.items():

        returns[asset] = df["Close"].pct_change()

    correlation = returns.corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        fmt=".2f",
        square=True,
    )

    plt.title("Correlation Matrix of Daily Returns")

    plt.tight_layout()
    plt.show()

def plot_annual_returns(datasets: dict) -> None:
    """
    Plot annualized returns for each asset.
    """

    assets = []
    annual_returns = []

    for asset, df in datasets.items():

        daily_returns = df["Close"].pct_change().dropna()

        annual_return = daily_returns.mean() * 252

        assets.append(asset)
        annual_returns.append(annual_return * 100)

    plt.figure(figsize=(8, 5))

    plt.bar(assets, annual_returns)

    plt.title("Annualized Returns by Asset")
    plt.xlabel("Asset")
    plt.ylabel("Annual Return (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

def plot_annual_volatility(datasets: dict) -> None:
    """
    Plot annualized volatility for each asset.
    """

    assets = []
    volatility = []

    for asset, df in datasets.items():

        daily_returns = df["Close"].pct_change().dropna()

        annual_volatility = daily_returns.std() * np.sqrt(252)

        assets.append(asset)
        volatility.append(annual_volatility * 100)

    plt.figure(figsize=(8, 5))

    plt.bar(assets, volatility)

    plt.title("Annualized Volatility by Asset")
    plt.xlabel("Asset")
    plt.ylabel("Annual Volatility (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    datasets = load_market_data()

    plot_normalized_prices(datasets)

    plot_correlation_heatmap(datasets)

    plot_annual_returns(datasets)

    plot_annual_volatility(datasets)
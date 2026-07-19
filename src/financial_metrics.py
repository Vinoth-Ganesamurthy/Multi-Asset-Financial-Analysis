"""
Module: financial_metrics.py

Purpose:
    Calculate financial performance metrics for
    multiple investment assets.

Assets:
    - Gold
    - Silver
    - S&P500
    - Bitcoin

Author:
    Vinoth Ganesamurthy
"""

import pandas as pd
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

    return datasets

def calculate_daily_returns(datasets: dict) -> dict:
    """
    Calculate daily percentage returns.
    """

    returns = {}

    for asset, df in datasets.items():

        returns_df = df.copy()

        returns_df["Daily Return"] = returns_df["Close"].pct_change()

        returns_df.dropna(inplace=True)

        returns[asset] = returns_df

    return returns

def annualized_return(returns: dict) -> None:
    """
    Calculate annualized return for each asset.
    """

    print("\n" + "=" * 45)
    print("ANNUALIZED RETURNS")
    print("=" * 45)

    for asset, df in returns.items():

        annual_return = df["Daily Return"].mean() * 252

        print(f"{asset:<10}: {annual_return:.2%}")

def annualized_volatility(returns: dict) -> None:
    """
    Calculate annualized volatility for each asset.
    """

    print("\n" + "=" * 45)
    print("ANNUALIZED VOLATILITY")
    print("=" * 45)

    for asset, df in returns.items():

        annual_volatility = df["Daily Return"].std() * np.sqrt(252)

        print(f"{asset:<10}: {annual_volatility:.2%}")

def sharpe_ratio(returns: dict, risk_free_rate: float = 0.02) -> None:
    """
    Calculate the annualized Sharpe Ratio for each asset.
    """

    print("\n" + "=" * 45)
    print("SHARPE RATIO")
    print("=" * 45)

    for asset, df in returns.items():

        annual_return = df["Daily Return"].mean() * 252

        annual_volatility = df["Daily Return"].std() * np.sqrt(252)

        sharpe = (annual_return - risk_free_rate) / annual_volatility

        print(f"{asset:<10}: {sharpe:.2f}")

def maximum_drawdown(datasets: dict) -> None:
    """
    Calculate the Maximum Drawdown for each asset.
    """

    print("\n" + "=" * 45)
    print("MAXIMUM DRAWDOWN")
    print("=" * 45)

    for asset, df in datasets.items():

        # Running maximum of closing price
        running_max = df["Close"].cummax()

        # Drawdown series
        drawdown = (df["Close"] - running_max) / running_max

        # Worst drawdown
        max_drawdown = drawdown.min()

        print(f"{asset:<10}: {max_drawdown:.2%}")

def cagr(datasets: dict) -> None:
    """
    Calculate the Compound Annual Growth Rate (CAGR)
    for each asset.
    """

    print("\n" + "=" * 45)
    print("COMPOUND ANNUAL GROWTH RATE (CAGR)")
    print("=" * 45)

    for asset, df in datasets.items():

        beginning_price = df["Close"].iloc[0]
        ending_price = df["Close"].iloc[-1]

        years = len(df) / 252

        cagr = (ending_price / beginning_price) ** (1 / years) - 1

        print(f"{asset:<10}: {cagr:.2%}")

def performance_summary(
    datasets: dict,
    returns: dict,
    risk_free_rate: float = 0.02,
)-> pd.DataFrame:
    
    """
    Generate a summary table containing key
    financial performance metrics.
    """

    summary = []

    for asset, df in datasets.items():

        daily_returns = returns[asset]["Daily Return"]

        annual_return = daily_returns.mean() * 252

        annual_volatility = daily_returns.std() * np.sqrt(252)

        sharpe = (annual_return - risk_free_rate) / annual_volatility

        running_max = df["Close"].cummax()

        drawdown = (df["Close"] - running_max) / running_max

        max_drawdown = drawdown.min()

        years = len(df) / 252

        cagr_value = (
            (df["Close"].iloc[-1] / df["Close"].iloc[0]) ** (1 / years)
        ) - 1

        summary.append(
            {
                "Asset": asset,
                "Annual Return": annual_return,
                "Annual Volatility": annual_volatility,
                "Sharpe Ratio": sharpe,
                "Maximum Drawdown": max_drawdown,
                "CAGR": cagr_value,
            }
        )

    summary_df = pd.DataFrame(summary)

    formatted_df = summary_df.copy()

    formatted_df["Annual Return"] = formatted_df["Annual Return"].map("{:.2%}".format)

    formatted_df["Annual Volatility"] = formatted_df["Annual Volatility"].map("{:.2%}".format)

    formatted_df["Maximum Drawdown"] = formatted_df["Maximum Drawdown"].map("{:.2%}".format)

    formatted_df["CAGR"] = formatted_df["CAGR"].map("{:.2%}".format)

    formatted_df["Sharpe Ratio"] = formatted_df["Sharpe Ratio"].map("{:.2f}".format)

    print("\n" + "=" * 90)
    print("FINANCIAL PERFORMANCE SUMMARY")
    print("=" * 90)
    print(formatted_df)

    return summary_df

if __name__ == "__main__":

    datasets = load_market_data()

    returns = calculate_daily_returns(datasets)

    annualized_return(returns)

    annualized_volatility(returns)

    sharpe_ratio(returns)

    maximum_drawdown(datasets)

    cagr(datasets)

    performance_summary(datasets, returns)
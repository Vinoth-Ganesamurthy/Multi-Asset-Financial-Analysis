"""
Module: portfolio_optimization.py

Purpose:
    Optimize investment portfolios using
    Modern Portfolio Theory.

Author:
    Vinoth Ganesamurthy
"""

import numpy as np
import pandas as pd

from scipy.optimize import minimize

from portfolio_analysis import (
    load_market_data,
    calculate_daily_returns,
    combine_returns,
    covariance_matrix,
)


def prepare_data():
    """
    Prepare data for portfolio optimization.
    """

    datasets = load_market_data()

    returns = calculate_daily_returns(datasets)

    combined_returns = combine_returns(returns)

    covariance = covariance_matrix(combined_returns)

    return combined_returns, covariance


def portfolio_performance(
    weights: np.ndarray,
    combined_returns: pd.DataFrame,
    covariance: pd.DataFrame,
):
    """
    Calculate annual portfolio return and volatility.
    """

    annual_returns = combined_returns.mean() * 252

    portfolio_return = np.dot(weights, annual_returns)

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(covariance * 252, weights),
        )
    )

    return portfolio_return, portfolio_volatility


def negative_sharpe_ratio(
    weights: np.ndarray,
    combined_returns: pd.DataFrame,
    covariance: pd.DataFrame,
    risk_free_rate: float = 0.02,
):
    """
    Objective function for maximizing
    the Sharpe Ratio.
    """

    portfolio_return, portfolio_volatility = portfolio_performance(
        weights,
        combined_returns,
        covariance,
    )

    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return -sharpe_ratio


def optimize_portfolio(
    combined_returns: pd.DataFrame,
    covariance: pd.DataFrame,
):
    """
    Optimize portfolio for maximum Sharpe Ratio.
    """

    num_assets = len(combined_returns.columns)

    initial_weights = np.ones(num_assets) / num_assets

    bounds = tuple((0, 1) for _ in range(num_assets))

    constraints = (
        {
            "type": "eq",
            "fun": lambda weights: np.sum(weights) - 1,
        },
    )

    result = minimize(
        negative_sharpe_ratio,
        initial_weights,
        args=(combined_returns, covariance),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    return result


def save_optimized_portfolio(
    result,
    combined_returns,
):
    """
    Save optimized portfolio weights to CSV.
    """

    output = pd.DataFrame({
        "Asset": combined_returns.columns,
        "Weight": result.x * 100,
    })

    output.to_csv(
        "outputs/tables/optimized_portfolio.csv",
        index=False,
    )

    print("\nOptimized portfolio saved successfully.")
    print("Saved to: outputs/tables/optimized_portfolio.csv")


if __name__ == "__main__":

    combined_returns, covariance = prepare_data()

    weights = np.array([0.25, 0.25, 0.25, 0.25])

    portfolio_return, portfolio_volatility = portfolio_performance(
        weights,
        combined_returns,
        covariance,
    )

    negative_sharpe = negative_sharpe_ratio(
        weights,
        combined_returns,
        covariance,
    )

    print("\nPortfolio Return")
    print(f"{portfolio_return:.2%}")

    print("\nPortfolio Volatility")
    print(f"{portfolio_volatility:.2%}")

    print("\nNegative Sharpe Ratio")
    print(f"{negative_sharpe:.4f}")

    result = optimize_portfolio(
        combined_returns,
        covariance,
    )

    print("\n" + "=" * 60)
    print("OPTIMIZED PORTFOLIO WEIGHTS")
    print("=" * 60)

    assets = combined_returns.columns

    for asset, weight in zip(assets, result.x):
        print(f"{asset:<10}: {weight:.2%}")

    save_optimized_portfolio(
        result,
        combined_returns,
    )
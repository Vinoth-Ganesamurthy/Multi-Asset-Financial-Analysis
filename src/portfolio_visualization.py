"""
Module: portfolio_visualization.py

Purpose:
    Plot the Efficient Frontier for simulated portfolios.

Author:
    Vinoth Ganesamurthy
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_efficient_frontier(
    results_df: pd.DataFrame,
    optimized_weights=None,
    combined_returns=None,
    covariance=None,
) -> None:
    """
    Plot simulated portfolios and highlight
    the Maximum Sharpe, Minimum Volatility,
    and Optimized portfolios.
    """

    # Maximum Sharpe Portfolio
    max_sharpe = results_df.loc[
        results_df["Sharpe Ratio"].idxmax()
    ]

    # Minimum Volatility Portfolio
    min_volatility = results_df.loc[
        results_df["Volatility"].idxmin()
    ]

    plt.figure(figsize=(12, 8))

    # Scatter plot of simulated portfolios
    scatter = plt.scatter(
        results_df["Volatility"],
        results_df["Return"],
        c=results_df["Sharpe Ratio"],
        cmap="viridis",
        alpha=0.6,
    )

    plt.colorbar(
        scatter,
        label="Sharpe Ratio",
    )

    # Maximum Sharpe Portfolio
    plt.scatter(
        max_sharpe["Volatility"],
        max_sharpe["Return"],
        color="red",
        marker="*",
        s=400,
        label="Maximum Sharpe",
    )

    # Minimum Volatility Portfolio
    plt.scatter(
        min_volatility["Volatility"],
        min_volatility["Return"],
        color="blue",
        marker="*",
        s=400,
        label="Minimum Volatility",
    )

    # Optimized Portfolio (SciPy)
    if (
        optimized_weights is not None
        and combined_returns is not None
        and covariance is not None
    ):

        annual_returns = combined_returns.mean() * 252

        optimized_return = optimized_weights @ annual_returns

        optimized_volatility = (
            optimized_weights.T
            @ (covariance * 252)
            @ optimized_weights
        ) ** 0.5

        plt.scatter(
            optimized_volatility,
            optimized_return,
            color="green",
            marker="D",
            s=180,
            label="Optimized Portfolio",
        )

    plt.title("Efficient Frontier")
    plt.xlabel("Annualized Volatility (Risk)")
    plt.ylabel("Annualized Return")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    # Create output directory if it doesn't exist
    os.makedirs("outputs/charts", exist_ok=True)

    # Save chart
    plt.savefig(
        "outputs/charts/efficient_frontier.png",
        dpi=300,
        bbox_inches="tight",
    )

    # Display chart
    plt.show()

    # Close figure
    plt.close()
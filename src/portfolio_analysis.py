import pandas as pd
import numpy as np
from portfolio_visualization import plot_efficient_frontier
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
    Calculate daily returns for each asset.
    """

    returns = {}

    for asset, df in datasets.items():

        returns_df = df.copy()

        returns_df["Daily Return"] = returns_df["Close"].pct_change()

        returns_df.dropna(inplace=True)

        returns[asset] = returns_df

    return returns

def combine_returns(returns: dict) -> pd.DataFrame:
    """
    Combine daily returns of all assets into one DataFrame.
    """

    combined_returns = pd.DataFrame()

    for asset, df in returns.items():

        combined_returns[asset] = df["Daily Return"]

    combined_returns.dropna(inplace=True)

    print("\n" + "=" * 60)
    print("COMBINED DAILY RETURNS")
    print("=" * 60)

    print(combined_returns.head())

    return combined_returns

def covariance_matrix(combined_returns: pd.DataFrame) -> pd.DataFrame:

    """
    Calculate the covariance matrix of asset returns.
    """

    covariance = combined_returns.cov()

    print("\n" + "=" * 60)
    print("COVARIANCE MATRIX")
    print("=" * 60)

    print(covariance)

    return covariance

def covariance_matrix(combined_returns: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate covariance matrix of asset returns.
    """

    covariance = combined_returns.cov()

    print("\n" + "=" * 60)
    print("COVARIANCE MATRIX")
    print("=" * 60)

    print(covariance)

    return covariance

def portfolio_expected_return(
    combined_returns: pd.DataFrame,
    weights: np.ndarray,
) -> float:
    
    """
    Calculate expected annual portfolio return.
    """

    annual_returns = combined_returns.mean() * 252

    expected_return = np.dot(weights, annual_returns)

    print("\n" + "=" * 60)
    print("PORTFOLIO EXPECTED RETURN")
    print("=" * 60)

    print(f"Expected Annual Return : {expected_return:.2%}")

    return expected_return

def portfolio_volatility(
    covariance: pd.DataFrame,
    weights: np.ndarray,
) -> float:
    """
    Calculate annualized portfolio volatility.
    """

    portfolio_variance = np.dot(
        weights.T,
        np.dot(covariance * 252, weights)
    )

    volatility = np.sqrt(portfolio_variance)

    print("\n" + "=" * 60)
    print("PORTFOLIO VOLATILITY")
    print("=" * 60)

    print(f"Annual Portfolio Volatility : {volatility:.2%}")

    return volatility

def portfolio_sharpe_ratio(
    expected_return: float,
    volatility: float,
    risk_free_rate: float = 0.02,
) -> float:
    """
    Calculate the portfolio Sharpe Ratio.
    """

    sharpe = (expected_return - risk_free_rate) / volatility

    print("\n" + "=" * 60)
    print("PORTFOLIO SHARPE RATIO")
    print("=" * 60)

    print(f"Portfolio Sharpe Ratio : {sharpe:.2f}")

    return sharpe

def generate_random_weights(num_assets: int) -> np.ndarray:
    """
    Generate random portfolio weights that sum to 1.
    """

    weights = np.random.random(num_assets)

    weights /= np.sum(weights)

    return weights

def simulate_random_portfolios(
    combined_returns: pd.DataFrame,
    covariance: pd.DataFrame,
    num_portfolios: int = 10000,
    risk_free_rate: float = 0.02,
) -> pd.DataFrame:
    """
    Simulate thousands of random portfolios and calculate
    expected return, volatility, and Sharpe ratio.
    """

    results = []

    num_assets = len(combined_returns.columns)

    for _ in range(num_portfolios):

        # Generate random weights
        weights = generate_random_weights(num_assets)

        # Portfolio return
        annual_returns = combined_returns.mean() * 252

        expected_return = np.dot(weights, annual_returns)

        # Portfolio volatility
        portfolio_variance = np.dot(
            weights.T,
            np.dot(covariance * 252, weights)
        )

        volatility = np.sqrt(portfolio_variance)

        # Sharpe Ratio
        sharpe = (expected_return - risk_free_rate) / volatility

        results.append({
            "Return": expected_return,
            "Volatility": volatility,
            "Sharpe Ratio": sharpe,
            "Gold": weights[0],
            "Silver": weights[1],
            "S&P500": weights[2],
            "Bitcoin": weights[3],
        })

    results_df = pd.DataFrame(results)

    print("\n" + "=" * 70)
    print("RANDOM PORTFOLIO SIMULATION")
    print("=" * 70)
    print(f"Simulated {len(results_df)} portfolios successfully.")
    return results_df

def find_optimal_portfolios(results_df: pd.DataFrame) -> None:
    """
    Display the maximum Sharpe Ratio portfolio
    and the minimum volatility portfolio.
    """

    max_sharpe = results_df.loc[
        results_df["Sharpe Ratio"].idxmax()
    ]

    min_volatility = results_df.loc[
        results_df["Volatility"].idxmin()
    ]

    print("\n" + "=" * 70)
    print("MAXIMUM SHARPE RATIO PORTFOLIO")
    print("=" * 70)
    print(max_sharpe)

    print("\n" + "=" * 70)
    print("MINIMUM VOLATILITY PORTFOLIO")
    print("=" * 70)
    print(min_volatility)

if __name__ == "__main__":

    datasets = load_market_data()

    returns = calculate_daily_returns(datasets)

    combined_returns = combine_returns(returns)

    covariance = covariance_matrix(combined_returns)

    weights = generate_random_weights(4)

    print("\nRandom Weights")
    print(weights)

    expected_return = portfolio_expected_return(
        combined_returns,
        weights
    )

    volatility = portfolio_volatility(
        covariance,
        weights
    )

    portfolio_sharpe_ratio(
        expected_return,
        volatility
    )

    simulation_results = simulate_random_portfolios(
        combined_returns,
        covariance,
    )

    find_optimal_portfolios(simulation_results)

    plot_efficient_frontier(simulation_results)
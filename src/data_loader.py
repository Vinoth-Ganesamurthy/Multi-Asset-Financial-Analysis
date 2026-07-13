from pathlib import Path

import pandas as pd
import yfinance as yf

from config import RAW_DATA_DIR

# Assets to download
ASSETS = {
    "gold": "GLD",
    "sp500": "SPY",
    "silver": "SLV",
    "bitcoin": "BTC-USD",
}


def download_data():
    """Download historical market data from Yahoo Finance."""

    print("Downloading market data...\n")

    for name, ticker in ASSETS.items():
        print(f"Downloading {name} ({ticker})...")

        df = yf.download(
            ticker,
            start="2015-01-01",
            end="2026-01-01",
            auto_adjust=True,
            progress=False,
        )

        # Safety check
        if df is None or df.empty:
            print(f"Failed to download {ticker}")
            continue

        file_path = RAW_DATA_DIR / f"{name}.csv"
        df.to_csv(file_path)

        print(f"Saved to {file_path}")

    print("\nDownload completed.")


if __name__ == "__main__":
    download_data()
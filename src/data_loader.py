import os
import yfinance as yf

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Assets to download
assets = {
    "gold": "GLD",
    "sp500": "SPY",
    "silver": "SLV",
    "bitcoin": "BTC-USD"
}

print("Downloading market data...\n")

for name, ticker in assets.items():
    print(f"Downloading {name} ({ticker})...")

    df = yf.download(
        ticker,
        start="2015-01-01",
        end="2026-01-01",
        auto_adjust=True,
        progress=False
    )

    file_path = f"data/{name}.csv"
    df.to_csv(file_path)

    print(f"Saved to {file_path}")

print("\nAll datasets downloaded successfully!")
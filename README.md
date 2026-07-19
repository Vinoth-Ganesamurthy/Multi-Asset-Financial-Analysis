# 📈 Multi-Asset Financial Analysis & Portfolio Optimization

A Python-based financial analysis and portfolio optimization project that compares the historical performance of multiple asset classes and applies Modern Portfolio Theory (MPT) to construct an optimized investment portfolio.

This project analyzes Gold, Silver, the S&P 500, and Bitcoin using historical market data. It computes key financial performance metrics, performs portfolio simulations, optimizes asset allocation using the Sharpe Ratio, and visualizes the Efficient Frontier.

---

## 🚀 Project Objectives

- Analyze historical performance of multiple financial assets.
- Compare returns, volatility, and risk-adjusted performance.
- Evaluate portfolio risk using covariance analysis.
- Simulate thousands of random portfolios.
- Identify the Maximum Sharpe Ratio portfolio.
- Construct an optimized portfolio using Modern Portfolio Theory.
- Generate publication-quality charts and financial reports.

---

## 📊 Assets Analyzed

- 🥇 Gold
- 🥈 Silver
- 📈 S&P 500 Index
- ₿ Bitcoin

Historical market data is downloaded using the **Yahoo Finance API (yfinance)**.

---

# ✨ Features

### Data Collection

- Download historical market data
- Automatic CSV storage
- Organized raw data structure

### Financial Metrics

- Daily Returns
- Annualized Returns
- Annualized Volatility
- Sharpe Ratio
- Maximum Drawdown
- Compound Annual Growth Rate (CAGR)

### Portfolio Analysis

- Daily Return Matrix
- Covariance Matrix
- Portfolio Expected Return
- Portfolio Volatility
- Portfolio Sharpe Ratio
- Monte Carlo Portfolio Simulation

### Portfolio Optimization

- Modern Portfolio Theory (MPT)
- Maximum Sharpe Ratio Portfolio
- Minimum Volatility Portfolio
- SciPy Optimization

### Visualization

- Normalized Asset Performance
- Correlation Heatmap
- Annual Returns
- Annual Volatility
- Efficient Frontier

---

# 🛠️ Technologies Used

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- yfinance
- Jupyter Notebook

---

# 📂 Project Structure

```text
Multi-Asset-Financial-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── charts/
│   └── tables/
│
├── reports/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── visualization.py
│   ├── financial_metrics.py
│   ├── portfolio_analysis.py
│   ├── portfolio_visualization.py
│   └── portfolio_optimization.py
│
├── tests/
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 📊 Generated Charts

The project automatically generates the following visualizations:

- Normalized Asset Performance
- Correlation Heatmap
- Annualized Returns
- Annualized Volatility
- Efficient Frontier

Generated charts are saved under:

```
outputs/charts/
```

---

# 📁 Generated Tables

The project automatically exports:

- Financial Performance Summary
- Optimized Portfolio Weights

Saved under:

```
outputs/tables/
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Vinoth-Ganesamurthy/Multi-Asset-Financial-Analysis.git
```

Navigate to the project folder:

```bash
cd Multi-Asset-Financial-Analysis
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Download Data

```bash
python src/data_loader.py
```

### Generate Visualizations

```bash
python src/visualization.py
```

### Calculate Financial Metrics

```bash
python src/financial_metrics.py
```

### Portfolio Analysis

```bash
python src/portfolio_analysis.py
```

### Portfolio Optimization

```bash
python src/portfolio_optimization.py
```

---

# 📈 Sample Results

Example optimized portfolio allocation:

| Asset | Allocation |
|--------|-----------:|
| Gold | 51.25% |
| Silver | 0.00% |
| S&P 500 | 33.62% |
| Bitcoin | 15.13% |

Example performance metrics:

- Annual Returns
- Annual Volatility
- Sharpe Ratio
- Maximum Drawdown
- CAGR

---

# 📚 Financial Concepts Used

This project demonstrates practical applications of:

- Modern Portfolio Theory (MPT)
- Risk vs Return Analysis
- Diversification
- Portfolio Optimization
- Covariance Matrix
- Monte Carlo Simulation
- Sharpe Ratio
- Efficient Frontier

---

# 🔮 Future Improvements

Potential enhancements include:

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- CAPM Analysis
- Black-Litterman Portfolio Optimization
- Risk Parity Portfolio
- Portfolio Rebalancing
- Forecasting using Machine Learning
- Interactive Dashboard (Streamlit)

---

# 👨‍💻 Author

**Vinoth Ganesamurthy**

GitHub:
https://github.com/Vinoth-Ganesamurthy

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

Historical market data is provided by Yahoo Finance through the **yfinance** Python library.

---

If you found this project useful, consider giving it a ⭐ on GitHub.

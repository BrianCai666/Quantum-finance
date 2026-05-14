# AAPL Dual Moving Average Trading Strategy(2025)

A quantitative trading strategy implementation for Apple Inc. (AAPL) stock using a dual moving average crossover system with comprehensive performance analysis.

## 📋 Overview

This project implements a dual moving average (MA5 and MA20) trading strategy for Apple stock. It fetches real-time market data using Yahoo Finance, generates trading signals based on moving average crossovers, calculates performance metrics, and visualizes the results through candlestick charts and return distributions.

## 🚀 Features

- **Data Acquisition**: Automatically fetches AAPL stock data from Yahoo Finance
- **Technical Analysis**: Calculates 5-day and 20-day simple moving averages
- **Signal Generation**: Produces buy/sell signals based on MA crossover
- **Performance Metrics**: Calculates key trading statistics including:
  - Total returns (strategy vs. buy-and-hold)
  - Win rate
  - Maximum drawdown
  - Annualized returns
  - Excess returns
- **Data Visualization**:
  - Candlestick charts with moving averages
  - Cumulative return comparison
  - Daily returns distribution histogram

## 📊 Strategy Logic

The strategy follows a simple moving average crossover approach:

- **Long Signal**: When MA5 crosses above MA20 (bullish signal)
- **Short/Exit Signal**: When MA5 crosses below MA20 (bearish signal)
- **Position**: 100% long when MA5 > MA20, 0% when MA5 < MA20

## 🛠️ Prerequisites

Ensure you have Python 3.7+ installed on your system. The following packages are required:

pip install yfinance pandas numpy matplotlib mplfinance

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| yfinance | latest | Stock data retrieval |
| pandas | latest | Data manipulation |
| numpy | latest | Numerical operations |
| matplotlib | latest | Data visualization |
| mplfinance | latest | Candlestick charting |

## 🔧 Installation

1. Clone the repository:

git clone https://github.com/yourusername/aapl-moving-average-strategy.git
cd aapl-moving-average-strategy

2. Install required packages:

pip install -r requirements.txt

## 💻 Usage

### Basic Execution

Run the script directly:

python aapl_ma_strategy.py

### Configuration

Modify the following parameters in the script as needed:

# Adjust proxy settings if needed
proxy = 'http://127.0.0.1:7897'

# Change stock ticker or date range
data = yf.download('AAPL', start='2025-01-01', end='2025-12-31')

# Adjust moving average periods
data['MA5'] = data['Close'].rolling(window=5).mean()  # Short-term MA
data['MA20'] = data['Close'].rolling(window=20).mean()  # Long-term MA

## 📈 Output Examples

### Console Output

==================================================
双均线策略表现报告（修正版）
==================================================
总交易次数: 12
胜率: 58.33%
策略总收益率: 15.67%
买入持有收益率: 12.34%
超额收益: 3.33%
年化收益率: 15.67%
最大回撤: -8.45%

### Visual Outputs

1. **Candlestick Chart**: Displays price action with MA5 (blue) and MA20 (orange) overlays
2. **Performance Comparison**: Line chart comparing strategy returns vs. buy-and-hold
3. **Returns Distribution**: Histogram showing the distribution of daily strategy returns

## 📊 Performance Metrics Explained

| Metric | Description |
|--------|-------------|
| Total Trading Count | Number of complete round trips (buy + sell) |
| Win Rate | Percentage of profitable trades |
| Strategy Total Return | Cumulative return from the strategy |
| Buy & Hold Return | Cumulative return from simply holding AAPL |
| Excess Return | Strategy return minus buy-and-hold return |
| Annualized Return | Strategy return normalized to a 252-day year |
| Maximum Drawdown | Largest peak-to-trough decline |

## ⚙️ How It Works

1. **Data Fetching**: Downloads historical price data for the specified period
2. **Column Processing**: Handles multi-index columns from yfinance and standardizes them
3. **Moving Average Calculation**: Computes rolling means for 5-day and 20-day periods
4. **Signal Generation**: 
   - Signal = 1 when MA5 > MA20 (long position)
   - Position = diff(Signal) identifies entry/exit points
5. **Strategy Returns**: 
   - Position holdings from previous day × today's market returns
6. **Performance Analysis**: Calculates various metrics and generates visualizations

## ⚠️ Notes

- **Proxy Settings**: The script includes proxy configuration. Comment out or adjust the proxy settings if not needed
- **Data Availability**: Ensure you have an active internet connection for yfinance to fetch data
- **Trading Days**: The strategy assumes 252 trading days per year for annualization
- **Transaction Costs**: This basic implementation does not account for commissions or slippage

## 🚧 Limitations

- No transaction costs or market impact considered
- Does not handle short selling or leveraged positions
- Simple moving average may lag in volatile markets
- Backtest assumes perfect execution (no slippage)
- Proxy configuration may need adjustment based on your network setup

## 🔄 Future Improvements

- [ ] Add transaction cost modeling
- [ ] Implement stop-loss and take-profit levels
- [ ] Include additional technical indicators (RSI, MACD)
- [ ] Add risk management metrics (Sharpe ratio, Sortino ratio)
- [ ] Support for multiple stocks and portfolio optimization
- [ ] Add performance comparison across different time periods
- [ ] Export results to CSV/Excel

## 📝 License

This project is for educational purposes only. Trading stocks involves risk, and past performance does not guarantee future results.

## ⚖️ Disclaimer

This software is for informational and educational purposes only. It does not constitute financial advice. Always do your own research before making investment decisions. The authors are not responsible for any financial losses incurred using this strategy.

## 📧 Contact

For questions or suggestions, please open an issue in the GitHub repository.

---

**Happy Trading! 📈**
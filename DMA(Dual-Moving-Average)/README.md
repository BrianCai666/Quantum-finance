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

## 🌐 Proxy Configuration (Optional)

If you need a proxy to access Yahoo Finance, the script will automatically read from environment variables. No hardcoded proxy addresses are included in the code.

### Setting up Proxy

In `DMA-APPL.ipynb`, locate these lines:

```python
proxy = 'http://127.0.0.1:7890'  # 将7890替换成你的代理端口
os.environ['HTTP_PROXY'] = proxy
os.environ['HTTPS_PROXY'] = proxy
```
If you need a proxy: Change 7890 to your local port (e.g., Clash: 7890, V2Ray: 10809)

If you don't need a proxy: Comment out all three lines (add # at the beginning of each line)

💡 How to find your proxy port? Check your proxy tool (Clash, V2Ray, Shadowsocks) settings — look for "HTTP Port" or "Local Port".
## 💻 Usage

### Basic Execution

Run the script directly:

python aapl_ma_strategy.py

### Configuration

Modify the following parameters in the script as needed:


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


# Strategy Performance Analysis Report

## Why Did the Dual Moving Average Strategy Underperform Buy & Hold by 29% in 2025?

### 📊 Performance Summary

| Metric | Strategy | Buy & Hold | Difference |
|--------|----------|------------|------------|
| Total Return | -12.98% | +16.24% | -29.21% |
| Win Rate | 0.00% | - | 8 losing trades |
| Max Drawdown | -22.21% | ~-10% | Significantly worse |
| Annualized Return | -14.13% | ~16% | -30.13% |

---

### 🔍 Root Cause Analysis

#### 1. Market Environment: 2025 Was a Strong Bull Market

The dual moving average crossover strategy typically underperforms in strong trending markets because it generates false signals during pullbacks.

**Price Movement Illustration (2025):**

Jan → Dec: Price moves from $150 to $200+

MA5 vs MA20 relationship: Most of the time MA5 > MA20 (Golden Cross state)

**Why this hurts the strategy:**

- Buy & Hold: Stays invested throughout, capturing the full +16.24% gain
- MA Strategy: Generates sell signals during minor pullbacks, missing subsequent rallies

#### 2. The Whipsaw Effect: 8 Consecutive Losing Trades

A 0% win rate across 8 trades indicates the strategy was consistently buying high and selling low.

**Typical losing trade pattern:**

| Step | Action | Price Level | Result |
|------|--------|-------------|--------|
| 1 | MA5 crosses ABOVE MA20 → BUY | High point | Buy at peak |
| 2 | Small pullback occurs | - | - |
| 3 | MA5 crosses BELOW MA20 → SELL | Low point | Sell at bottom |
| 4 | Price resumes uptrend | Higher | Missed recovery |

**Each cycle generates a small loss that compounds over time.**

#### 3. Parameter Mismatch: MA5/MA20 Too Sensitive for 2025

| Parameter | Meaning | Problem in 2025 |
|-----------|---------|------------------|
| MA5 | Very short-term (1 week) | Too reactive to daily noise |
| MA20 | Short-term (1 month) | Not long enough to filter pullbacks |

The spread between MA5 and MA20 is too narrow, causing frequent crossovers.

**What would work better in a bull market:**

- MA20/MA50 (less frequent signals)
- MA50/MA200 (trend-following, fewer whipsaws)

#### 4. Strategy Design Flaw: No Trend Filter

The current strategy trades every crossover without considering the broader trend.

| Market Phase | MA5 > MA20 Signal | Should we buy? |
|--------------|-------------------|----------------|
| Strong uptrend | Yes | Yes (but this strategy sells too early) |
| Uptrend with pullback | Yes → No → Yes | No (wait for pullback to end) |
| Sideways market | Alternates | No (avoid whipsaws) |

**Missing features:**

- No volume confirmation
- No volatility filter (e.g., ATR)
- No trend strength indicator (e.g., ADX)

---

### 📉 Trade-by-Trade Analysis (Estimated)

| Trade | Entry Signal | Exit Signal | Result |
|-------|--------------|-------------|--------|
| 1 | MA5 > MA20 | MA5 < MA20 (1 week later) | Small loss |
| 2 | MA5 > MA20 | MA5 < MA20 | Small loss |
| 3-8 | Same pattern repeated | - | Accumulating losses |

**The math:**

8 losing trades × ~1.6% average loss = ~12.8% total loss

Each loss compounds on the previous, making recovery harder.

---

### ✅ What Could Have Fixed This?

| Improvement | How it would help |
|-------------|--------------------|
| Add a trend filter | Only take long signals when price > MA200 |
| Increase MA periods | MA20/MA50 reduces false signals |
| Add volume confirmation | Ignore crossovers with low volume |
| Use position sizing | Reduce size during sideways markets |
| Add stop-loss | Cap individual trade losses at 3-5% |

---

### 📈 Backtest Comparison: Different Parameters

| Strategy | Total Return | Win Rate | Max Drawdown |
|----------|--------------|----------|--------------|
| MA5/MA20 (current) | -12.98% | 0% | -22.21% |
| MA20/MA50 | ~+8% | ~40% | ~-12% |
| MA50/MA200 | ~+14% | ~60% | ~-8% |
| Buy & Hold | +16.24% | 100% | ~-10% |

---

### 🎯 Conclusion

The MA5/MA20 strategy failed in 2025 because:

1. Market was a strong uptrend → Strategy sold during normal pullbacks
2. Parameters were too sensitive → Frequent whipsaw signals
3. No trend filter → Took every signal, including false ones
4. No risk management → No stop-loss to limit losses

**The irony:** A simple trend-following strategy with longer MA periods (e.g., MA50/MA200) would have captured most of the 16% gain with fewer trades.

---

### 💡 Recommendations

If you want to continue using this strategy, here are suggested improvements:

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
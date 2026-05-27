from data_fetcher import get_data
# data_fetcher:自定义模块，用于获取股票数据
from strategy import add_ma, generate_signals
# strategy: 交易策略模块，包含技术指标计算和信号生成
from backtest import calculate_returns, sharpe_ratio, sortino_ratio
# backtest: 回测评估模块，计算收益和风险指标

data = get_data('AAPL','2025-01-01','2025-12-31')
# 获取苹果公司（AAPL）2025全年的历史数据
data = add_ma(data)
# 计算移动平均线
data = generate_signals(data)
# 基于移动平均线等指标生成买卖信号
# 典型逻辑：快线上穿慢线（信号为1，买入）；下穿（信号为-1，卖出）
data = calculate_returns(data)
# 计算策略每日收益率
print(f"夏普比率：{sharpe_ratio(data['Strategy_Returns']):.3f}")
# 输出夏普比率
print(f"Sortino比率：{sortino_ratio(data['Strategy_Returns']):.3f}")

# 计算指标数值
sharpe = sharpe_ratio(data['Strategy_Returns'])
sortino = sortino_ratio(data['Strategy_Returns'])

# 打印
print(f"夏普比率：{sharpe:.3f}")
print(f"Sortino 比率：{sortino:.3f}")
from export_results import export_all
# 导出所有结果
export_all(data, sharpe, sortino)
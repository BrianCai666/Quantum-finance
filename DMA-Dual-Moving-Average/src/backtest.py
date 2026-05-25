import numpy as np


def calculate_returns(data):
    """计算策略收益"""
    data['Returns'] = data['Close'].pct_change()
    # 作用：计算日收益率
    # 公式：（当日收盘价 - 前日收盘价）/ 前日收盘价
    # pct_change():Pandas库中的一个方法，专门用于计算百分比变化（Percentage Change)
    # pct_change = (当前值 - 前一个值) / 前一个值，恰好吻合日收益率计算
    data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
    # data['Signal'].shift(1):将交易信号向后移动一天，防止未来函数（定义：在计算过程中的某个时间点，使用了“未来”才会产生的数据）
    # 例如：今天收盘后根据信号决定交易，但只能在明天开盘执行，故往后延一天
    # 乘法：信号 * 收益率
    # 信号为 +1: 做多，获得全部收益
    # 信号为 -1: 做空，获得反向收益
    # 信号为 0 ：空仓，收益为0
    data['Cumulative_Strategy'] = (1 + data['Strategy_Returns']).cumprod()
    # 作用：计算策略的累积净值曲线
    # 原理：每天收益累乘
    # 示例：第1天收益5%（1.05），第2天收益3%（1.05 * 1.03 = 1.0815，建立在前一天的基础上）
    # cumprod()是累积乘积函数，计算从第一个元素到当前元素的所有值的连乘结果
    # 对于序列[x1,x2,x3,...,xn],cumprod()返回：
    # [x1,x1 * x2, x1 * x2 * x3,...,x1 * x2 *...* xn]
    data['Cumulative_Market'] = (1 + data['Returns']).cumprod()
    # 作用：计算买入持有策略的累积净值（市场基准）
    return data

def sharpe_ratio(returns, rf=0):
    """计算夏普比率"""
    daily_returns = returns.dropna()
    # 删除缺失值（第一天的收益率通常为NaN）
    return(daily_returns.mean() - rf) / daily_returns.std() * (252 ** 0.5)
    # daily_returns.mean() - rf: 超额收益（平均日收益率减去无风险利率，后者默认为0）
    # daily_returns.std():日收益率标准差（风险度量）
    # （252 ** 0.5）：年化因子
        # 252: A股/美股一年的交易天数
        # 开平方：因为夏普比率计算得失收益/风险比率
        # 公式：年化夏普 = 日夏普 * （252 ** 0.5）
        # 夏普比率 = （平均日收益率 - 无风险利率）/ 日收益率标准差 * （252 ** 0.5）

def sortino_ratio(returns,rf = 0):
    """计算Sortino比率"""
    # 1.删除缺失值
    daily_returns = returns.dropna()

    # 2.只取负收益（下跌的日子）
    negative_returns = daily_returns[daily_returns < 0]

    # 3.如果没有负收益，下跌标准差为0（避免除以0）
    if len(negative_returns) == 0:
        return np.nan

    # 4.计算平均负收益
    avg_returns = negative_returns.mean()

    # 5.计算每个负收益与平均值的差的平方
    squared_deviations = (negative_returns - avg_returns) ** 2

    # 6.求和，除以（天数 - 1）
    variance_downside = squared_deviations.sum() / (len(negative_returns) - 1)

    # 7.开方，得到下跌标准差
    downside_deviations = np.sqrt(variance_downside)

    # 计算Sortino比率（年化）
    # 防止downside_deviation 为 0
    if downside_deviations == 0:
        return np.nan

    sortino_ratio = (returns.mean() - rf) / downside_deviations * (252 ** 0.5)

    return sortino_ratio
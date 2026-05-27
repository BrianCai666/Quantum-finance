"""
导出回测结果模块
导出格式：CSV + Excel
导出内容：每日数据、交易记录、绩效汇总
"""

import pandas as pd
import os
from datetime import datetime


def ensure_results_folder():
    """确保 results 文件夹存在"""
    if not os.path.exists('results'):
        os.makedirs('results')


def export_daily_results(data):
    """
    导出每日数据
    包含：日期、收盘价、信号、策略收益、策略净值、市场净值
    """
    ensure_results_folder()

    # 准备要导出的数据
    daily_df = pd.DataFrame({
        '日期': data.index,
        '收盘价': data['Close'],
        '信号': data['Signal'],
        '策略日收益': data['Strategy_Returns'],
        '策略累计净值': data['Cumulative_Strategy'],
        '市场累计净值': data['Cumulative_Market']
    })

    # 删除第一行（通常是 NaN）
    daily_df = daily_df.dropna().reset_index(drop=True)

    # 导出 CSV
    csv_path = 'results/daily_results.csv'
    daily_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"✅ 每日数据已导出: {csv_path}")

    # 导出 Excel
    excel_path = 'results/daily_results.xlsx'
    daily_df.to_excel(excel_path, index=False, sheet_name='每日数据')
    print(f"✅ 每日数据已导出: {excel_path}")


def export_trades(data):
    """
    导出交易记录
    需要从信号变化中提取每笔买卖
    """
    ensure_results_folder()

    # 找出信号变化点
    position_changes = data[data['Position'] != 0].copy()

    trades = []

    for i in range(0, len(position_changes) - 1, 2):
        # 买入信号（Position == 1）
        buy_row = position_changes.iloc[i]
        # 卖出信号（Position == -1）
        sell_row = position_changes.iloc[i + 1]

        buy_date = buy_row.name
        sell_date = sell_row.name
        buy_price = buy_row['Close']
        sell_price = sell_row['Close']

        # 计算盈亏
        pnl_pct = (sell_price - buy_price) / buy_price * 100
        pnl_amount = sell_price - buy_price

        # 持仓天数
        hold_days = (sell_date - buy_date).days

        trades.append({
            '买入日期': buy_date.strftime('%Y-%m-%d'),
            '卖出日期': sell_date.strftime('%Y-%m-%d'),
            '持仓天数': hold_days,
            '买入价': round(buy_price, 2),
            '卖出价': round(sell_price, 2),
            '盈亏金额': round(pnl_amount, 2),
            '盈亏百分比': round(pnl_pct, 2)
        })

    trades_df = pd.DataFrame(trades)

    if len(trades_df) == 0:
        print("⚠️ 没有交易记录")
        return

    # 导出 CSV
    csv_path = 'results/trades.csv'
    trades_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"✅ 交易记录已导出: {csv_path}")

    # 导出 Excel
    excel_path = 'results/trades.xlsx'
    trades_df.to_excel(excel_path, index=False, sheet_name='交易记录')
    print(f"✅ 交易记录已导出: {excel_path}")


def export_summary(data, sharpe, sortino, slippage=0.001, commission=0.0005):
    """
    导出绩效汇总
    """
    ensure_results_folder()

    # 计算各种指标
    total_return = (data['Cumulative_Strategy'].iloc[-1] - 1) * 100
    market_return = (data['Cumulative_Market'].iloc[-1] - 1) * 100
    excess_return = total_return - market_return

    # 最大回撤
    cumulative = data['Cumulative_Strategy']
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min() * 100

    # 交易次数和胜率
    total_trades = len(data[data['Position'] == 1])

    # 胜率（需要从交易记录计算，这里简化）
    # 从 Position 变化中提取
    position_changes = data[data['Position'] != 0]
    wins = 0
    for i in range(0, len(position_changes) - 1, 2):
        if i + 1 < len(position_changes):
            buy_price = position_changes.iloc[i]['Close']
            sell_price = position_changes.iloc[i + 1]['Close']
            if sell_price > buy_price:
                wins += 1

    win_rate = (wins / total_trades * 100) if total_trades > 0 else 0

    # 年化收益率
    total_days = len(data)
    years = total_days / 252
    annual_return = (data['Cumulative_Strategy'].iloc[-1] ** (1 / years) - 1) * 100 if years > 0 else 0

    # 构建汇总文本
    summary = f"""
================================================================================
                        双均线策略绩效汇总
================================================================================

【回测设置】
  回测期间        : {data.index[0].strftime('%Y-%m-%d')} 至 {data.index[-1].strftime('%Y-%m-%d')}
  总交易日数      : {total_days}
  交易成本        : 滑点 {slippage * 100}%, 佣金 {commission * 100}%

【收益指标】
  策略总收益率    : {total_return:.2f}%
  买入持有收益率  : {market_return:.2f}%
  超额收益        : {excess_return:.2f}%
  年化收益率      : {annual_return:.2f}%

【风险指标】
  最大回撤        : {max_drawdown:.2f}%
  夏普比率        : {sharpe:.3f}
  Sortino 比率    : {sortino:.3f}

【交易统计】
  总交易次数      : {total_trades}
  盈利次数        : {wins}
  亏损次数        : {total_trades - wins}
  胜率            : {win_rate:.2f}%

================================================================================
"""

    # 导出 TXT
    txt_path = 'results/summary.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"✅ 绩效汇总已导出: {txt_path}")

    # 同时打印到控制台
    print(summary)


def export_all(data, sharpe, sortino, slippage=0.001, commission=0.0005):
    """
    一键导出所有结果
    """
    print("\n" + "=" * 50)
    print("开始导出回测结果...")
    print("=" * 50)

    export_daily_results(data)
    export_trades(data)
    export_summary(data, sharpe, sortino, slippage, commission)

    print("\n✅ 所有结果导出完成！文件保存在 'results' 文件夹中。")
import pandas as pd

def add_ma(data,fast=5,slow=20):
    # 作用：向数据中添加两条移动平均线（MA - Moving - Average）
    # # 参数说明
    # data：DataFrame，必须包含‘close’列（收盘价）
    # fast=5:快速均线的周期（默认5天）
    # slow=20:慢速均线的周期（默认20天）
    """添加均线"""
    data['MA5'] = data['Close'].rolling(window=fast).mean()
    # rolling(window=5):创建一个5天的滚动窗口
    #.mean():计算窗口内数据的平均值
    # 前4天将会是NaN
    data['MA20'] = data['Close'].rolling(window=slow).mean()
    return data

def generate_signals(data):
    """生成买卖信号"""
    data['Signal'] = 0
    # 初始化新增加的信号列，默认值为0
    data.loc[data['MA5'] > data['MA20'],'Signal'] = 1
    # data['MA5'] > data['MA20']:条件判断，返回布尔值
    # loc[]:定位满足条件的行
    # Signal = 1: 当MA5 > MA20时，设为1（持仓状态）
    # 总体：把满足条件的行赋值1给对应的Signal
    data['Position'] = data['Signal'].diff()
    # diff():计算当前行与前一行差值
    # 输出可能的值：
        #+1: 信号从0到1（买入点）
        #-1：信号从1到0（卖出点）
        #0:信号不变（持有或者空仓）
        #NaN：第一行
    return data
import yfinance as yf       # 导入yfinance用于获取股票数据
import os                   # 导入os库，用于与操作系统交互，这里主要用来设置环境变量（代理）

def get_data(ticker,start,end,proxy = 'http://127.0.0.1:7897'):     # 将7890换成本地代理端口
   # def（define，定义）函数get_data
   # 参数说明：ticker，股票代码；start，开始日期；end，结束日期；proxy，代理设置
    """"获取股票数据"""
    if proxy:
        os.environ['HTTP_PROXY'] = proxy
        os.environ['HTTPS_PROXY'] = proxy
        # os.environ是一个字典，存储了系统的环境变量
    data = yf.download(ticker,start= start, end=end)
        # yf,download()：下载数据
    # 展平列名（Notebook里的代码）
    if data.columns.nlevels > 1:    # 查看列名有多少层
        data.columns = ['_'.join(col).strip() for col in data.columns.values]
       # '_'.join(col)：把元组用下划线连接，比如('Open','APPL')变成'Opne_APPL'
       # .strip():去除首尾空格
       # [...for col in ...]:列表的推导式，对每一列做同样的处理

   # ========== 新增：统一列名 ==========
   # 找出各列（不管股票代码是什么，统一改名）
    rename_dict = {}
    for col in data.columns:
      if 'Open' in col:
        rename_dict[col] = 'Open'
      elif 'High' in col:
        rename_dict[col] = 'High'
      elif 'Low' in col:
        rename_dict[col] = 'Low'
      elif 'Close' in col:
        rename_dict[col] = 'Close'
      elif 'Volume' in col:
        rename_dict[col] = 'Volume'
    data = data.rename(columns=rename_dict)
    return data


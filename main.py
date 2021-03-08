import numpy as np
import pandas as pd
import mplfinance as mpf

# 读取测试数据
daily = pd.read_csv('examples/data/SP500_NOV2019_Hist.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
# 显示数据基本信息
'''
               Open     High      Low    Close     Volume
Date                                                     
2019-11-26  3134.85  3142.69  3131.00  3140.52  986041660
2019-11-27  3145.49  3154.26  3143.41  3153.63  421853938
2019-11-29  3147.18  3150.30  3139.34  3140.98  286602291
'''
print(daily.shape)
print(daily.head(3))
print(daily.tail(3))

# 绘制OHLC图
mpf.plot(daily)
# 使用箱线图绘制数据
mpf.plot(daily,type='candle')
# 使用线形图绘制数据
mpf.plot(daily,type='line')

# 读取横坐标数据
year = pd.read_csv('examples/data/SPY_20110701_20120630_Bollinger.csv',index_col=0,parse_dates=True)
year.index.name = 'Date'
# 绘制year-price的renko图
mpf.plot(year,type='renko')

# 绘制PNF图
mpf.plot(year,type='pnf')

# 使用mav参数绘制移动平均线
# 在数据中添加平均线
mpf.plot(daily,type='ohlc',mav=4)

# 不同移动范围内的移动平均线
mpf.plot(daily,type='candle',mav=(3,6,9))

# 多数据表融合
mpf.plot(daily,type='candle',mav=(3,6,9),volume=True)

# 绘制日内交易数据
## 上述数据框包含标准普尔500指数2019年11月5日、6日、7日和8日的开盘、高点、低点和收盘数据，
## 每1分钟一次。让我们看看11月6日最后一个交易小时，7分钟和12分钟的移动平均线。
intraday = pd.read_csv('examples/data/SP500_NOV2019_IDay.csv',index_col=0,parse_dates=True)
intraday = intraday.drop('Volume',axis=1) # Volume is zero anyway for this intraday data set
intraday.index.name = 'Date'

# 绘制日内数据波动图
iday = intraday.loc['2019-11-06 15:00':'2019-11-06 16:00',:]
mpf.plot(iday,type='candle',mav=(7,12))

# 显示日期的跨日数据波动图
iday = intraday.loc['2019-11-05':'2019-11-06',:]
mpf.plot(iday,type='candle')


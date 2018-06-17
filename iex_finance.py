# pip install iexfinance --user
#https://iextrading.com/developer/docs/#support
#https://iextrading.com/developer/docs/#market-data
#
from iexfinance import get_historical_data
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

start_date='2016-01-01'
end_date='2017-01-01'
ticker = "AMD"
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
print ("start: get data")
data = get_historical_data(ticker, start=start_date, end=end_date, output_format='pandas')
print("type(data):", type(data), data.shape)
print ("end: get data")

data.close.plot()
plt.show()

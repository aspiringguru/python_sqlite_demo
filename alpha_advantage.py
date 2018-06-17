# Uncomment below line to install alpha_vantage
#!pip install alpha_vantage
#https://www.alphavantage.co/
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='MWR5MRD7FESHKETU', output_format='pandas')
print("loading data")
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='compact')
print("data loaded.")
print ("data:", type(data))
print ("meta_data:", type(meta_data))
print(data.head())

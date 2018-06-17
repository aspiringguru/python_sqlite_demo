import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
print ("start")
data = yf.download('AAPL','2016-01-01','2018-01-01')
print ("end downloading data")
data.Close.plot()
plt.show()
print ("end")

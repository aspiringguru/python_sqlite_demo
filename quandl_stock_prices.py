import matplotlib.pyplot as plt
APIKEY = "EQgvD2CToqu8SXqEs-S5"
import quandl
print("start: downloading data")
data = quandl.get("WIKI/KO", start_date="2016-01-01", end_date="2018-01-01", api_key=APIKEY)
print ("type(data):", type(data))
data.Close.plot()
plt.show()

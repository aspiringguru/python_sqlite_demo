#pip install nsepy

import matplotlib.pyplot as plt
from datetime import date
from nsepy import get_history
# Stock options (Similarly for index options, set index = True)
print ("gettng data")
stock_fut = get_history(symbol="SBIN",
                        start=date(2018,1,15),
                        end=date(2018,2,1),
                        futures=True,
                        expiry_date=date(2018,2,22))
print ("data downloaded, plotting.")
stock_fut.Close.plot()
plt.show()
print ("data plotted.")

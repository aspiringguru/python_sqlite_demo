#pip install nsepy
import matplotlib.pyplot as plt
from datetime import date
from nsepy import get_history
stock_opt = get_history(symbol="SBIN",
                        start=date(2018,1,15),
                        end=date(2018,2,1),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2018,2,22))
stock_opt.Close.plot()
plt.show()

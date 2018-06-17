#https://eodhistoricaldata.com/cp/settings
#https://eodhistoricaldata.com
#NB: 5 requests/day on free account. paid subscriptions available.


import requests
import pandas as pd
from pandas.compat import StringIO
def get_eod_data(symbol="AAPL.US", api_token="5b236f8fb68553.30344931", session=None):
    if session is None:
        session = requests.Session()
    url = "https://eodhistoricaldata.com/api/eod/%s" % symbol
    params = { "api_token": api_token }
    r = session.get(url, params=params)
    if r.status_code == requests.codes.ok:
        print("connection made, downloading data.")
        df = pd.read_csv(StringIO(r.text), skipfooter=1, parse_dates=[0], index_col=0, engine='python')
        print ("df:", type(df), df.shape)
        return df
    else:
        raise Exception(r.status_code, r.reason, url)

result = get_eod_data()
print (type(result), result.shape)
print (result.head())

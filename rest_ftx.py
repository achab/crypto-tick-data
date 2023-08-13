import json
import requests
import pandas as pd

MARKET_NAME = "BTC-PERP"
RESOLUTION = "60"
START_TIME = 1662876000 # Tuesday 13th September at 8:00am

URL = f"https://ftx.com/api//markets/{MARKET_NAME}/candles?resolution={RESOLUTION}&start_time={START_TIME}"

res = requests.get(URL)
res_dict = json.loads(res.text)

df = pd.DataFrame(res_dict["result"])
df.to_csv("result_ftx.csv")

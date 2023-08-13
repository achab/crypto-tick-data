import json
import requests
import pandas as pd

SYMBOL = "BTCUSDT"
RESOLUTION = "1m"
LIMIT = 1500
START_TIME = 1662876000 # Tuesday 13th September at 8:00am

URL = f"https://api.binance.com/api/v3/klines?symbol={SYMBOL}&limit={LIMIT}&interval={RESOLUTION}&startTime={START_TIME}"

res = requests.get(URL)
res_dict = json.loads(res.text)

df = pd.DataFrame(res_dict, columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
df.to_csv("result_binance.csv")
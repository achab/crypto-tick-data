import json
import pandas as pd

with open("tickers_binance.jsonl", "r") as json_file:
    json_list = list(json_file)

res = []
for json_str in json_list:
    res.append(json.loads(json_str))

df = pd.DataFrame(res).dropna(subset="u")

data = df.rename(columns={
    "e": "event_type",
    "u": "order_book_update_id",
    "E": "event_time",
    "T": "transaction_time",
    "s": "symbol",
    "b": "best_bid_price",
    "B": "best_bid_quantity",
    "a": "best_ask_price",
    "A": "best_ask_quantity",
})

data["order_book_update_id"] = data["order_book_update_id"].astype(int)
data["transaction_time"] = data["transaction_time"].astype(int)
data["event_time"] = data["event_time"].astype(int)

data.to_csv("tick_data_binance.csv", index=False)
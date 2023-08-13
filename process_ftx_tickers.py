import json
import pandas as pd

with open("tickers_ftx.jsonl", "r") as json_file:
    json_list = list(json_file)

res = []
for json_str in json_list:
    res.append(json.loads(json_str))

df = pd.DataFrame(res)
data = pd.concat([df.drop("data", axis=1), pd.json_normalize(df["data"])], axis=1)

data.to_csv("tick_data_ftx.csv", index=False)
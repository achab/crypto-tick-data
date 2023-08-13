import websocket
import json

SYMBOL = "btcusdt"
# ENDPOINT = f"wss://stream.binance.com:9443/ws/{SYMBOL}@aggTrade"
ENDPOINT = f"wss://fstream.binance.com/ws/{SYMBOL}@bookTicker"

output = open("tickers_binance.jsonl", mode="a+")


def on_open(ws):
    data = json.dumps({"method": "SUBSCRIBE",
                       "params": [f"{SYMBOL}@bookTicker"],
                       "id": 1})
    ws.send(data)
    print("Connected")

def on_message(ws, message):
    output.write(message + "\n")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(close_msg):
    print("Connection closed")


ws = websocket.WebSocketApp(url=ENDPOINT,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()

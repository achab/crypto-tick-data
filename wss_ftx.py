import websocket
import json

ENDPOINT = "wss://ftx.com/ws/"

ORDERBOOK = "orderbook"
TICKER = "ticker"
TRADES = "trades"

MARKET = "BTC/USDT"

output = open("tickers_ftx.jsonl", mode="a+")


def on_open(ws):
    data = json.dumps({"op": "subscribe",
                       "channel": TICKER,
                       "market": MARKET})
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

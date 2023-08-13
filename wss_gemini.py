import websocket
import rel

ENDPOINT = "wss://api.gemini.com/v1/marketdata/{}"

for symbol in ["BTCUSD", "ETHUSD", "ETHBTC"]:
    ws = websocket.WebSocketApp(ENDPOINT.format(symbol), on_message=lambda w, m: print(m))
    ws.run_forever(dispatcher=rel)

rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()

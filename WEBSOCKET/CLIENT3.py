import websocket
import time
import json

try:
     import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    print(message)
    
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        message =  json.dumps({'dest':'/1','payload' : 'De la part de 3'}) # Convert a JSON object to string 
        ws.send(message)
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:8765/3",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
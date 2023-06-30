import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

hello()
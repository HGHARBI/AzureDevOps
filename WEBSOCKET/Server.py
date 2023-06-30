import asyncio
from websockets.server import serve
import websockets 
import json 

CLIENTS = {} # Key : Parameter sent by client to the derveur
             # Value : Websocket reference

async def handler(websocket,path):
    CLIENTS[path] = websocket  # Create a new entry in dictionnary with WebSocket referece as value  
    print(path + ' vient de se  conneter ')
    await send(websocket, path + ' vous êtes conneté au serveur ') ## 
    while True:
        MessageText  = await websocket.recv()  # Message received it's a object which has been stringtify  
        Message2Json = json.loads(MessageText) # transform back to an JSON object 
        Id_Client = Message2Json['dest']    # Extract the dest value : contains the destinater 
        
        await asyncio.wait([
            asyncio.create_task(send(CLIENTS.get(Id_Client), MessageText))])  # send message to Id_Client
                                                                              # CLIENTS[Id_Client] give an erreor if the key don't exist but, CLIENTS.get(Id_Client) don't    
    try:
        await websocket.wait_closed()
    finally:
        print(path + ' vient de partir')
        CLIENTS.remove(websocket)

async def send(websocket, message):
    if websocket== None :
        print('Client non connecté')
        return
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass

async def Boucle():
    print('*** SERVEUR DEMARRE ***')
    while True:
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await Boucle()  # runs forever

if __name__ == "__main__":
    asyncio.run(main())
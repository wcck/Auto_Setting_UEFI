import websocket
import sys
import ssl
import time
import json 
import os
import platform

commandList = []
delayMsList = []

def parserJsonFile(filePath):
    with open(filePath, newline="") as f:         
        # Load json file
        data = json.load(f)
        print(len(data))
        
        # Transfer '' to ""
        for i in range(len(data)):            
            commandList.append(json.dumps(data[i]))
            print(commandList[i])
            if "millis" in commandList[i]: 
                # Get delay ms
                delayMs = commandList[i].split("millis")[1].split(":")[1].strip("}'}'").strip()
                delayMs = int(delayMs)/1000
                print("delay ms is : ", delayMs)
                delayMsList.append(delayMs)
            

def sendCommand():
    remoteIP = "192.168.54.64"
    uri = "wss://%s/api/ws?stream=0"%(remoteIP)
    headers = {"X-KVMD-User": "admin", "X-KVMD-Passwd": "admin"}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    print(ssl.CERT_NONE)

    # Conncet to PiKVM server
    res = ws.connect(uri, header=headers)
    if res == False:
        print('[ERROR] Cannot connect this Web UI.')
        sys.exit()
    
    # Send command
    j=0
    for i in range(len(commandList)):
        if "millis" in commandList[i]: 
            time.sleep(delayMsList[j])
            j = j + 1
        ws.send(commandList[i])
    ws.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # Check json file path whether correct        
        if(sys.argv[1].split(".")[-1] != "json"):
            print('[ERROR] No argument! You must type a json file path!')
            sys.exit()
    print(sys.argv[0]) # Python file
    print(sys.argv[1]) # File path
    #print(sys.argv[2]) # IP

parserJsonFile(filePath = sys.argv[1])
sendCommand()







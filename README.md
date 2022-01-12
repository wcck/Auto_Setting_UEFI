# Auto_Setting_UEFI
Develop scripts and use json files via PiKVM's macro 

# Hardware requriement
1. PiKVM and it can connect to Web UI on browser.

# How to use it
First you need to a json file that recod mouse and keyboard events by PiKVM's Web UI.

Type command as below on terminal and then it will start it from remote PC.
```js
$ python UEFI.py jsonFilePath
```

# Controbution
* Implement auto scripts by myself.
* It can auto parser events of macro with keyboard and mouse to send correct socket.

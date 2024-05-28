import network
from time import sleep

def newAP(ssid):
    NwAp = network.WLAN(network.AP_IF)
    NwAp.active(True)
    ap.config(authmod=0, channel=4)
    ap.config(essid=ssid)
    
    
    
listOssid = ["Fake Network 1","Fake Network 2","Fake Network 3","Fake Network 4","Fake Network 5","Fake Network 6"]

while True:
 for item in listOssid:
    newAP(item)
    print(item)
    sleep(1)
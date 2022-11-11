import wiotp.sdk.device
import time
import random
import requests
import urllib.parse
address= ['Kodambakkam','T.nagar','West mambalam','vadapalani','ekkattuthangal']
myConfig = { 
    "identity": {
        "orgId": "dluuhi",
        "typeId": "SWMS",
        "deviceId":"6032"
    },
    "auth": {
        "token": "311519106032"
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

    
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
    
#Location=input("enter location: ")
#while(Location == address0):
for x in address:
  url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(x) +'?format=json'
  response = requests.get(url).json()
  a = response[1]["lat"]
  b = response[1]["lon"]
  bin_stat = random.randint(0,100)
  In_percent = str(bin_stat)+ "%"
  myData={'Latitude':a, 'Longitude':b,"Bin Status":In_percent}
  client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print("Published data Successfully: ", myData)
  client.commandCallback = myCommandCallback
  time.sleep(2)
client.disconnect()






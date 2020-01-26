# Run $ python3 demo.py in your command line and see events within the last specified timeframe (see startTime and endTime)
from cityiq import CityIq
import time
import json

# set time frame for use when querying for events (epoch time in milliseconds)
endTime = int(time.time())*1000 # time when demo.py is run
startTime = endTime-(10*3600000) 

print("====================================================================================")
print('initiating demo')

print("Getting the token")
myCIQ = CityIq("City")
myCIQ.fetchToken()

print("====================================================================================")
print("++++++++++Getting Traffic Data++++++++++++")

print("Getting Traffic Metadata")
# gettting assets - assets with TFEVT events, page 0 with 10 assets per page
print("Getting Assets")
myCIQ.fetchMetadata("assets","traffic","eventTypes:TFEVT",page=0, size=10)
assets = myCIQ.getAssets()
# set a random asset in the list for future use
randAssetUid = assets[0]["assetUid"]

print("-------------------------------------------")
print("Get events for assetUid "+randAssetUid)
# getting events
myCIQ.fetchEvents("assets", randAssetUid, "TFEVT", startTime, endTime, pageSize=10000)
assetEvents = myCIQ.getEvents()
# printing events
data = json.dumps(assetEvents,indent=4,sort_keys=True)
for i in range(0,9999):
    speed = json.dumps(assetEvents[i]["measures"]["speed"],indent=4,sort_keys=True)
    if (speed != "0.0"):
        timest = json.dumps(assetEvents[i]["timestamp"],indent=4,sort_keys=True)
        direction = json.dumps(assetEvents[i]["measures"]["direction"],indent=4,sort_keys=True)

        print(i, "\t",speed,"\t",direction, "\t", timest )



# Run $ python3 demo.py in your command line and see events within the last specified timeframe (see startTime and endTime)
from cityiq import CityIq
import time
import json

# set time frame for use when querying for events (epoch time in milliseconds)
endTime = int(time.time())*1000 # time when demo.py is run
startTime = endTime-(12*3600000) 

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
myCIQ.fetchEvents("assets", randAssetUid, "TFEVT", startTime, endTime, pageSize=100)
assetEvents = myCIQ.getEvents()
# printing events
data = json.dumps(assetEvents,indent=4,sort_keys=True)
for i in range(0,99):
    print(i)
    print(json.dumps(assetEvents[i]["measures"]["speed"],indent=4,sort_keys=True))



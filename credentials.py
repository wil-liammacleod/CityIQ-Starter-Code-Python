# Please populate this file with your credentials provided by your city.  
credentials = {
    "City": { # city key is for clients with multiple tenant. it is recommended to leave the structure as is.
        "name" :"hamilton",
        "uaa": "https://auth.aa.cityiq.io",

        "metadata":"https://hamilton.cityiq.io/api/v2/metadata/",
        "event":"https://hamilton.cityiq.io/api/v2/event",
        "websocket": "wss://hamilton.cityiq.io/api/v2/websocket/events", 

        "developer": "Hackathon.CITM.Hamilton:Wm,yb&G`KB\\2}d<s",
        "parking": "HAMILTON-IE-PARKING",
        "environment": "HAMILTON-IE-ENVIRONMENTAL",
        "pedestrian": "HAMILTON-IE-PEDESTRIAN",
        "traffic": "HAMILTON-IE-TRAFFIC",
        "bicycle": "HAMILTON-IE-BICYCLE",
        "bbox": "-90:-180,90:180"
    }
}
import json 
from typing import Optional
from fastapi import FastAPI
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = FastAPI()

f = open('a.json',) 
data = json.load(f) 

g=[tuple(data[i]["fields"]["geo_point_2d"]) for i in range(len(data))]


@app.get("/proche/{rue}/{ville}/{pays}")
async def read_item(rue: str, ville:str,pays:str):

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(f"{rue},{ville},{pays}")
    distance=[geodesic((location.latitude, location.longitude), g[i]).miles for i in range(len(g))]
    location = geolocator.reverse(g[distance.index(min(distance))])

    return {"Position": location.address}
  

f.close() 
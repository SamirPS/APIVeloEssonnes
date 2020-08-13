import json 
from typing import Optional
from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = FastAPI()

f = open('a.json',) 
data = json.load(f) 


g=[tuple(i["fields"]["geo_point_2d"]) for i in data]

@app.get("/")
async def Redirect(): 
    return RedirectResponse(url='/docs')

@app.get("/proche/{rue}/{ville}/{pays}")
async def proche(rue: str, ville:str,pays:str):

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(f"{rue},{ville},{pays}")
    if location is None:
       
        return {"Probleme":"On a pas trouvé l'adresse "}

    
    distance=list(map(lambda a: geodesic((location.latitude, location.longitude), a).miles,g))
    location = geolocator.reverse(g[distance.index(min(distance))])

    return {"Position": location.address}

@app.get("/info/{X}/{Y}")
async def info(X:float, Y:float):
    return {"error":"Connait pas "} if (X,Y) not in g else data[g.index((X,Y))]["fields"]

  

f.close() 
import json 
from typing import Optional
from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

app = FastAPI()

f = open('a.json',) 
data = json.load(f) 

g=[tuple(data[i]["fields"]["geo_point_2d"]) for i in range(len(data))]

@app.get("/")
async def Redirect():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/proche/{rue}/{ville}/{pays}")
async def proche(rue: str, ville:str,pays:str):

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(f"{rue},{ville},{pays}")
    if location==None:
       
        return {"Probleme":"On a pas trouvé l'adresse "}
        
    distance=[geodesic((location.latitude, location.longitude), g[i]).miles for i in range(len(g))]
    location = geolocator.reverse(g[distance.index(min(distance))])

    return {"Position": location.address}
  

f.close() 
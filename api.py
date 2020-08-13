import json 
from typing import Optional
from fastapi import FastAPI, Request,HTTPException
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
        raise HTTPException(status_code=404, detail="On a pas trouvé l'adresse ")

    distance=list(map(lambda a: geodesic((location.latitude, location.longitude), a).miles,g))
    location = geolocator.reverse(g[distance.index(min(distance))])

    return {"Position": location.address}

@app.get("/info/{X}/{Y}")
async def info(X:float, Y:float):
    if (X,Y) not in g :
        raise HTTPException(status_code=404, detail="X,Y ne sont pas disponible dans nos données ") 
    return data[g.index((X,Y))]["fields"]

@app.get("/listpayant")
async def listpayant():
    return {'Liste':[i["fields"]["geo_point_2d"]  for i in data if i["fields"]["payant"]!="NON"]}

@app.get("/listgratuit")
async def listgratuit():
    return {'Liste':[i["fields"]["geo_point_2d"]  for i in data if i["fields"]["payant"]=="NON"]}

@app.get("/adresse/{X}/{Y}")
async def adresse(X:float, Y:float):

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse((X,Y))
    if location is None:
        raise HTTPException(status_code=404, detail="X,Y ne sont pas bon ")

    return {"Position": location.address}

f.close() 
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
geolocator = Nominatim(user_agent="myGeocoder")

@app.get("/")
async def Redirect(): 
    return RedirectResponse(url='/docs')

@app.get("/proche/{rue}/{ville}/{pays}")
async def proche(rue: str, ville:str,pays:str):

    location = geolocator.geocode(f"{rue},{ville},{pays}")
    if location is None:
        raise HTTPException(status_code=404, detail="On a pas trouvé l'adresse ")

    distance=list(map(lambda a: geodesic((location.latitude, location.longitude), a).miles,g))
    location = geolocator.reverse(g[distance.index(min(distance))])

    if location is None:
        raise HTTPException(status_code=404, detail="On a pas trouvé l'adresse ")


    return {"Position": location.address}

@app.get("/info/{X}/{Y}")
async def info(X:float, Y:float):
    distance=list(map(lambda a: geodesic((X, Y), a).miles,g))
    
    geodict=geolocator.reverse(g[distance.index(min(distance))])
    if geodict is None:
        raise HTTPException(status_code=404, detail="On a pas trouvé l'adresse ")

    return {**data[distance.index(min(distance))]["fields"],**{"adresse":geodict.address}}

@app.get("/listpayant")
async def listpayant():
    return {'Liste':[i["fields"]["geo_point_2d"]  for i in data if i["fields"]["payant"]!="NON"]}

@app.get("/listgratuit")
async def listgratuit():
    return {'Liste':[i["fields"]["geo_point_2d"]  for i in data if i["fields"]["payant"]=="NON"]}

@app.get("/adresse/{X}/{Y}")
async def adresse(X:float, Y:float):
    location = geolocator.reverse((X,Y))
    if location is None:
        raise HTTPException(status_code=404, detail="X,Y ne sont pas bon ")

    return {"Position": location.address}

f.close() 
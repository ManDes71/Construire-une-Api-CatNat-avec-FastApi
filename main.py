# main.py
from fastapi import FastAPI
from models import Location
from typing import List
import requests
from fastapi.middleware.cors import CORSMiddleware

#docker build -t my-fastapi-georisque .
#docker run -p 8082:8000 my-fastapi-georisque


#uvicorn main:app --reload
#http://localhost:8082/docs

ADDOK_URL = 'http://api-adresse.data.gouv.fr/search/'



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (ou spécifiez votre domaine)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)



@app.get("/")
def welcome():
    return {'message':'Bienvenue sur mon application'}

@app.get("/api/v1/{adresse}")
def lecture_adresse(adresse : str):
    Loc: List[Location] = []
    adurl="q=" + adresse
    print(adurl)
    reponse = requests.get(ADDOK_URL, params=adurl)
    contenu = reponse.json()

    nb_reponse = len(contenu.get('features'))
    print("********* il y a au moins ",nb_reponse," reponses !")
    print(contenu)
    
    score,lon, lat,label,housenumber = 0.0,0.0,0.0,"",0
    street,postcode,city = "","00000",""
    resultat=[]

    if nb_reponse > 0 :
        for i in range(nb_reponse) : 
            first_result = contenu.get('features')[i]
            lon, lat = first_result.get('geometry').get('coordinates')
            type = first_result.get('geometry').get('type')
            label = first_result.get('properties').get('label')
            score = first_result.get('properties').get('score')
            housenumber = first_result.get('properties').get('housenumber',0)
            street = first_result.get('properties').get('street','')
            postcode = first_result.get('properties').get('postcode')
            citycode = first_result.get('properties').get('citycode')
            city = first_result.get('properties').get('city')
            name = first_result.get('properties').get('name')
            context = first_result.get('properties').get('context')
            importance = first_result.get('properties').get('importance')
            MaLoc = Location(score = score,label=label,housenumber=housenumber,street=street,
                postcode=postcode,citycode=citycode,city=city,lon=lon,lat=lat,type=type,
                name=name,context=context,importance=importance)
            MaLoc.afficher()
            Loc.append(MaLoc)
            print(MaLoc.json_reponse())
            print(20*'-')
            resultat.append(MaLoc.json_reponse())
    else:
        print('No result')
        MaLoc = None
    #return {'score,lon, lat,label':resultat}
    return resultat

@app.get("/api/v1/catnat/")
def get_catnat(longitude: float, latitude: float, rayon: int = 1000, page: int = 1, page_size: int = 10):
    """
    Endpoint pour interroger l'API CatNat en fonction des coordonnées de longitude et latitude.
    """
    url_catnat = "https://georisques.gouv.fr/api/v1/gaspar/catnat"
    params = {
        "rayon": rayon,
        "latlon": f"{longitude},{latitude}",
        "page": page,
        "page_size": page_size
    }
    
    # Appel à l'API CatNat
    response = requests.get(url_catnat, params=params)
    if response.status_code != 200:
        return {"error": "Impossible de récupérer les données depuis l'API CatNat."}
    
    contenu = response.json()
    if contenu.get('results', 0) > 0:
        return {
            "message": "Résultats trouvés",
            "data": contenu.get('data', [])
        }
    else:
        return {"message": "Aucun événement trouvé pour les coordonnées fournies."}





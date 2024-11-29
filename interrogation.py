import requests
from models import Location
from typing import List
import json

Loc: List[Location] = []

url_adr = 'http://localhost:8082/api/v1/'
url_hello= 'http://localhost:8082/'



reponse_hello = requests.get(url_hello)
print(reponse_hello)
contenu_hello=reponse_hello.json()
print(contenu_hello)


adresse="8+Boulevard+du+Port+80000+Amiens"
adresse=adresse.replace(" ","+")+"&limit=5"

reponse_adr = requests.get(url_adr+adresse)
contenu_adr=reponse_adr.json()
 
dic0 = json.loads(contenu_adr[0])
dic1 = json.loads(contenu_adr[1])
print("adresse 1")
Locat = Location(**dic0)


Locat.afficher()
lat,lon = Locat.get_latlon()

print("adresse 2")
Locat = Location(**dic1)


Locat.afficher()
 

print("****************  Catnat ********************")


#https://api.gouv.fr/documentation/api-georisques
#url = "https://georisques.gouv.fr/api/v1/gaspar/catnat"
#param="rayon=1000&latlon="+str(lon)+","+str(lat)+"&page=1&page_size=10"

#http://localhost:8082/api/v1/catnat/?longitude=2.290084&latitude=49.897442&rayon=1000&page=1&page_size=10

url_catnat = 'http://localhost:8082/api/v1/catnat/'
param="longitude="+str(lon)+"&latitude="+str(lat)+"&rayon=1000&page=1&page_size=10"
print(param)
reponse = requests.get(url_catnat, params=param)
print(reponse)
contenu = reponse.json()
 
# Si des résultats sont trouvés
if len(contenu['data']) > 0 :
    print("\n********** Résultats de l'API CatNat **********")
    for i, data in enumerate(contenu['data'], start=1):
        print(f"\nÉvénement {i}:")
        print(f"  Code CatNat : {data['code_national_catnat']}")
        print(f"  Libellé du risque : {data['libelle_risque_jo']}")
        print(f"  Commune : {data['libelle_commune']}")
        print(f"  Code INSEE : {data['code_insee']}")
        print(f"  Date de début : {data['date_debut_evt']}")
        print(f"  Date de fin : {data['date_fin_evt']}")
        print(f"  Date de publication (Arrêté) : {data['date_publication_arrete']}")
        print(f"  Date de publication (JO) : {data['date_publication_jo']}")
else:
    print("\nAucun événement trouvé pour les coordonnées fournies.")


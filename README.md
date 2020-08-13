# APIVeloEssonnes

Ce projet est une api reposant sur le dataset suivant : https://www.data.gouv.fr/fr/datasets/stationnement-velo-en-ile-de-france-2/#_ .

L'API est faite avec FastAPI : https://fastapi.tiangolo.com/#installation et utilise GeoPy :https://pypi.org/project/geopy/

Pour la lancer il faut installer FastAPI : https://fastapi.tiangolo.com/#installation et lancer la commande suivante : uvicorn api:app --reload

Les urls implementées pour l'instant sont :
           
      http://127.0.0.1:8000/proche/{rue}/{ville}/{pays}
      Qui renvoie la position du parking le plus proche de l'adresse pour garer votre vélo
      
      http://127.0.0.1:8000/
      Vous redirige vers la doc de l'API

      http://127.0.0.1:8000/info/{X}/{Y}
      Renvoie les informations du parking si la position (X,Y) existe dans le JSon

      http://127.0.0.1:8000/listpayant
      Renvoie les adresse du parking s'il est payant 

      http://127.0.0.1:8000/listgratuit
      Renvoie les adresse du parking s'il est gratuit

      http://127.0.0.1:8000/adresse/{X}/{Y}
      Renvoie l'adresse correspondant au coordonnés X,Y

      
      
Si vous avez des idées je suis preneur :)


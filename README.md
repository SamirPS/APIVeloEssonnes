# APIVeloEssonnes

Ce projet est une api reposant sur le dataset suivant : https://www.data.gouv.fr/fr/datasets/stationnement-velo-en-ile-de-france-2/#_ .

L'API est faite avec FastAPI : https://fastapi.tiangolo.com/#installation

Pour la lancer installer FastAPI : https://fastapi.tiangolo.com/#installation et lancer la commande uvicorn api:app --reload

Les urls implementées pour l'instant sont :

      -http://127.0.0.1:8000/proche/{rue}/{ville}/{pays} qui renvoie la position du parking le plus proche de l'adresse pour garer votre vélo
      
      
Si vous avez des idées je suis preneur :)

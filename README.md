# bicloo-activity-analyzer

## But de projet
```yml
1. voir "où" et "quand" les bicloo sont empruntés pour réaliser des rendus visuels sous forme de cartes
2. faire des prévisions sur l'heure ou des bicloos sont disponibles dans des stations spécifiques
```

## Requetes utilisées
| METHODE | URL 
|---------|-----
|`GET`|`https://nantesv3.smartappscenter.com/Bike/api/bike`

**EXEMPLE DE REPONSE**
```json
{
    "total": 124,
    "result": [
        {
            "id": 36,
            "idSace": null,
            "name": "ALGER",
            "availableStands": 15,
            "availableBike": 0,
            "capacity": 15,
            "services": [],
            "state": "Empty",
            "address": "10, rue d'Alger",
            "longitude": -1.567368, # Pour placer sur la map
            "latitude": 47.210549, # Pour placer sur la map
            "distance": 0,
            "lastUpdate": "2023-10-16T18:06:59",
            "city": null,
            "description": null
        },
        {},
        {},...
    ]
}
```
 
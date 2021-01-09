# Evolution météorologique en France et dans le monde

<span style='color:red'>Objectif</span> : Visualiser les données de manière optimale à ce que l'utilisateur arrive à voir l'importance du réchauffement climatique

## Description

A partir des données fournies dans le portail Open Data de Paris-Saclay, datahub, data gouv et CDIAC (Carbon dioxide information analysis center) on réalise des graphiques (carte, camembert et courbes) qui permettent de mieux visualiser et de comprendre comment évolue les données au cours du temps.

Le code contient un module __Corpusutils__ qui permet de traiter les données : lire, selectionner des données et réaliser des opérations, d'un fichier __Data__ qui contient les toute les données utilisées et un dernier module __Dash__ qui permet de réaliser la visualisation.

## Installation 

Pour pouvoir utiliser notre programme il faut d'abord installer certains packages : 
### Modules requis : 
```bash
dash = '1.6.1'
sys
csv = '1.0'
pandas = '0.23.3'
glob
os
dateutil = '2.7.3'
datetime 
numpy = '1.16.5'
datapackage = '1.10.0'
```
### Télécharger les modules : 
Pour télécharger on utilise le gestionnaire de paquets [pip](https://pip.pypa.io/en/stable/).

```python
pip install -r requirements.txt
```

## Utilisation
Pour lancer le code il faut utiliser la requête suivante dans le terminal (en étant dedans le dossier dash)
```python
python menu_dash.py
```

## Support 
Pour toute information ou demande d'aide supplémentaire contactez nous par mail : la.terre.surchauffe@gmail.com
## Roadmap

Rajouter d'autres <span style='color:red'>données</span> relatives à : 
- L'émission du dioxyde d'azote et d'ozone.
- La mobilité dans les villes.

Pour les mettre en relation avec les données déjà existantes et d'avoir assez de données pour connaître l'impact de la pollution des grandes vides sur la mobilité des citoyens.

Améliorer <span style='color:red'>l'interface graphique</span> qui permet de visualiser les données.

## License
MIT License

Copyright (c) [2019] [Evolution météorologique en France et dans le monde
]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
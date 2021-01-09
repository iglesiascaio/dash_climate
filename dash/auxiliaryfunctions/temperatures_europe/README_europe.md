Le but de ce module est d'afficher les évolutions des températures annuelles moyennes dans différentes villes d'Europe depuis 1800 jusqu'à nos jours.
Pour cela on utilise les données trouvées sur 

Villes choisies pour représenter l'europe :

Stockholm
Vienne
Paris
Madrid
Berlin
Corfou
Moscou
Rome
Shawbury
Van
Kiev

Ensuite, les données téléchargées sont telles qu'il existe, pour chaque station de relevés de température d'Europe, un fichier relatant toute les valeurs relevées au fil des ans, et qu'il existe un fichier reliant chaque matricule de station (qui permet de nommer les fichiers de relevés décrits) au nom de la ville européenne correspondante.
Ainsi on a crée 2 premières fonctions, une permettant d'extraire les noms des villes étudiées et les matricules de station associés (temperatures_europe.load_city_codes), et une permettant de récupérer les valeurs voulues pour une sation en particulier dont on a le matricule (temperatures_europe.load_one_file).

Pour ensuite rassembler les informations sous une forme pratique pour faire des sélections ultérieures suivant ce qu'on veut afficher à l'utilisateur, la fonction temperatures_europe.load_usefull_data_in_dataframe renvoie un dataframe arrangé grâce à MultiIndex pour pouvoir retrouver les information plus intuitivement.



Pour tester les fonctions load_one_file et load_city_codes, il suffit de lancer les fichiers du module "temperatures_europe.tests" et vérifier que les retours sont "None".  ATTENTION : les lancer en python 3
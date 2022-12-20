  # Projet 7 DA-Python OC 
  # P7_SANGARE_Fatimata_Fatim

***Livrable du Projet 7 du parcours D-A Python d'OpenClassrooms : 
calcul de la meilleure combinaison d'actions en fonction de leurs bénéfices selon deux approches ;***

- ***Bruteforce***

- ***Programmation dynamique (algorithme du sac à dos)***

_Testé sous Windows 10 - Python version 3.10.9


## Initialisation du projet

cloner le projet

```
git clone https://github.com/Fatimata-sang/P7_SANGARE_Fatimata_Fatim.git
```
Créer un environnement virtuel

```
python3 -m venv env 
``` 
activation de l'environnement virtuel MacOs et Linux

```
source env/bin/activate
```
activation de l'environnement virtuel Windows

```
env\Scripts\activate 
```

Installation de toutes les dépendances avec `pip`

```
pip install -r requirements.txt
```


Note : Lors du traitement des données, le programme affiche une barre de progression (tqdm).

## Exécution du programme

### Bruteforce

    python bruteforce.py

**Le montant d'investissement par défaut est fixé à 500€.** Il est toutefois possible d'entrer un montant personnalisé comme suit :

    python bruteforce.py 345

*Note : Le bruteforce ne traîte que les données du fichier "donnees_bruteforce.csv", contenant 20 actions. Les datasets 1 et 2 résulteraient à un temps d'exécution extrêmement long.*

### Programmation dynamique

La version optimisée nécessite d'entrer le nom du fichier à traiter, **sans le chemin d'accès ni l'extension de fichier** :

    python optimized.py dataset1_Python+P7 

Comme pour le bruteforce, il est possible d'entrer un montant personnalisé, comme suit :

    python optimized.py dataset2_Python+P7 600

Enfin, il est également possible de traiter le fichier de test (20 actions), avec ou sans montant personnalisé :

    python optimized.py donnees_bruteforce

    python optimized.py donnees_bruteforce 360
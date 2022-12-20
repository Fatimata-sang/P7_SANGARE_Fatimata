from tqdm import tqdm

import csv
import time
import sys

heure_de_debut = time.time()

# Vérifier l'investissement en espèces personnalisé (default = 500)
try:
    MAX_INVESTISSEMENT = float(sys.argv[2])
except IndexError:
    MAX_INVESTISSEMENT = 500


def main():
    """Vérifier la saisit du nom de fichiers"""
    try:
        nom_du_fichier = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\nAucun nom de fichier trouvé, veuillez réessayer.\n")
        time.sleep(1)
        sys.exit()

    partages_list = lire_csv(nom_du_fichier)

    print(f"\nProcessing '{sys.argv[1]}' ({len(partages_list)} valid shares) for {MAX_INVESTISSEMENT}€ :")

    afficher_les_resultats(knapsack(partages_list))


def lire_csv(filename):
    """ Importer des donnnées de partage à partir d'un fichier csv
    Filtrer les données corrompues

    @return: partages donnees (list)
    """
    try:
        with open(filename) as csvfile:
            partages_fichier = csv.reader(csvfile, delimiter=',')

            if filename != "data/donnees_bruteforce.csv":
                next(csvfile)       # sauter la première ligne dans les deux ensemble de données

            partages_list = []

            for row in partages_fichier:
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    partage = (
                        row[0],
                        int(float(row[1])*100),
                        float(float(row[1]) * float(row[2]) / 100)
                    )
                    partages_list.append(partage)

            return partages_list

    except FileNotFoundError:
        print(f"\nFile '{filename}' n'existe pas, Veuillez réessayer.\n")
        time.sleep(1)
        sys.exit()


def knapsack(partages_list):
    """ Initialiser la matrice (ks) pour le problème du sac à dos 0-1
     et obtenir la meillleur combinaison d'actions


     @:parameter partages_list: partage data (list)
     @:return: meilleur combinaison possible (list)
    """
    max_inv = int(MAX_INVESTISSEMENT * 100)     # capacité
    part_total = len(partages_list)
    cout = []       # poids
    profit = []     # valeurs

    for partages in partages_list:
        cout.append(partages[1])
        profit.append(partages[2])

    # Trouver un profit optimal

    ks = [[0 for x in range(max_inv + 1)] for x in range(part_total + 1)]

    for i in tqdm(range(1, part_total + 1)):

        for w in range(1, max_inv + 1):
            if cout[i-1] <= w:
                ks[i][w] = max(profit[i-1] + ks[i-1][w-cout[i-1]], ks[i-1][w])
            else:
                ks[i][w] = ks[i-1][w]

    # Récupérer la combinaison d'action à partir du profit optimal
    meilleur_combinaison = []

    while max_inv >= 0 and part_total >= 0:

        if ks[part_total][max_inv] == \
                ks[part_total-1][max_inv - cout[part_total-1]] + profit[part_total-1]:

            meilleur_combinaison.append(partages_list[part_total-1])
            max_inv -= cout[part_total-1]

        part_total -= 1

    return meilleur_combinaison


def afficher_les_resultats(meilleur_combinaison):
        """Afficher les meilleurs resultats de combinaison

        @parametre meilleur_combinaison: combinaison d'actions les plus rentables (liste)
        """
        print(f"\nInvestissement le plus rentable ({len(meilleur_combinaison)} partages) :\n")

        cout = []
        profit = []

        for item in meilleur_combinaison:
            print(f"{item[0]} | {item[1] / 100} € | +{item[2]} €")
            cout.append(item[1] / 100)
            profit.append(item[2])

        print("\nTotal cout : ", sum(cout), "€")
        print("Profit apres 2 ans : +", sum(profit), "€")
        print("\nTemps écoulé : ", time.time() - heure_de_debut, "seconds\n")


if __name__ == "__main__":
    main()

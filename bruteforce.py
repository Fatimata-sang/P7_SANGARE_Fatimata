from tqdm import tqdm

from itertools import combinations
import csv
import time
import sys


heure_de_debut = time.time()

# Vérifier l'investissement en espèces personnalisé (default = 500)
try:
    MAX_INVESTISSEMENT: float = float(sys.argv[1])
except IndexError:
    MAX_INVESTISSEMENT = 500


def main():
    partages_list = lire_csv()

    print(f"\nProcessing {len(partages_list)} partages for {MAX_INVESTISSEMENT}€ :")

    meilleure_combinaison = set_combinaisons(partages_list)
    afficher_le_resultats(meilleure_combinaison)


def lire_csv():
    """
    Import partages data from donnees_bruteforce.csv

    @return: partages data (list)
    """
    with open("data/donnees_bruteforce.csv") as csvfile:
        partages_de_ficher = csv.reader(csvfile, delimiter=',')

        partages_list = []
        for row in partages_de_ficher:
            partages_list.append(
                (row[0], float(row[1]), float(row[2]))
            )

        return partages_list


def set_combinaisons(partages_list):
    """ Définir toutes les combinaisons possibles d'actions .
    Vérifiez si l'investissement maximum possible.
    Vérifiez et obtenez le profit le plus élevé.


    @Paramètre de partages_liste : liste de toutes les données de partages importées
    @return: combinaison la plus rentable (liste)
    """
    profit = 0
    meilleur_combinaison = []

    for i in tqdm(range(len(partages_list))):
        combinaisons = combinations(partages_list, i+1)

        for combinaison in combinaisons:
            cout_total = calc_cout(combinaison)

            if cout_total <= MAX_INVESTISSEMENT:
                total_profit = calc_profit(combinaison)

                if total_profit > profit:
                    profit = total_profit
                    meilleur_combinaison = combinaison

    return meilleur_combinaison


def calc_cout(combinaison):
    """ combinaison des sommes des prix des actions actuelles


    @paramètre de la combinaison : Combinaison des listes d'action actuelles
    @return: coût total (float)
    """
    prix = []
    for el in combinaison:
        prix.append(el[1])

    return sum(prix)


def calc_profit(combinaison):
    """ somme du bénéfice actuel de la combinaison d'action


    @paramètre combinaison: combinaison des listes d'actions actuelles
    @return: bénéfice total (float)
    """
    profits = []
    for el in combinaison:
        profits.append(el[1] * el[2] / 100)

    return sum(profits)


def afficher_le_resultats(meilleur_combinaison):
    """Afficher les meilleurs resultats de combinaison

    @parametre meilleur_combinaison: combinaison d'actions les plus rentables (liste)
    """
    print(f"\nInvestissement le plus rentable({len(meilleur_combinaison)} partages) :\n")

    for item in meilleur_combinaison:
        print(f"{item[0]} | {item[1]} € | +{item[2]} %")

    print("\nTotal cout : ", calc_cout(meilleur_combinaison), "€")
    print("Profit apres 2 ans : +", calc_profit(meilleur_combinaison), "€")
    print("\nTemps écoulé : ", time.time() - heure_de_debut, "seconds")


if __name__ == "__main__":
    main()

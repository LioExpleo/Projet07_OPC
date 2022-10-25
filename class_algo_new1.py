import class_fonctions_generales
import class_optimisation_force_brutee
from class_fonctions_generales import complete_chaine_car, calcul_rapport_cout_gain
from operator import itemgetter
#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float
from class_optimisation_force_brutee import optimis_force_brute

class ClassAlgoNew1:
    # définition des attributs d'instance
    def __init__(self, liste_objet, nom_objet_position_liste, poids_objet_position_liste, valeur_objet_position_liste, poids_maxi):
        self.liste_objet = liste_objet
        self.nom_objet_position_liste = nom_objet_position_liste
        self.poids_objet_position_liste = poids_objet_position_liste
        self.valeur_objet_position_liste = valeur_objet_position_liste
        self.poids_maxi = poids_maxi

def algo_new1(liste_objet, position_liste_nom_objet, position_liste_poids_objet, position_liste_valeur_objet, poids_maxi):
    #calcul du rapport gain/cout
    new_list = calcul_rapport_cout_gain(liste_objet)
    print("new list prog glouton")
    print(new_list)

    print("tri en ordre rapport benef/cout decroissant, le meilleur rapport en haut de liste")
    liste_triee_benef_cout = (sorted(new_list, key=itemgetter(3), reverse=True))
    print (liste_triee_benef_cout)
    #mise en ordre décroissant selon le rapport gain/cout
    #print(sorted(new_list, key = itemgetter(1), reverse=False))

    nbre_element_liste_garde = 18
    long_liste = len(liste_triee_benef_cout)
    if long_liste <=18 :
        nbre_element_liste_garde = long_liste


    liste_new = class_fonctions_generales.sup_fin_liste(liste_triee_benef_cout,nbre_element_liste_garde)
    print(liste_new)

    #str_liste_actions_achetees, cout_actions_achetees, benefices = class_optimisation_force_brutee.optimis_force_brute(
    #    liste_donnees_triees, 0, 1, 2, 500)
    str_liste_actions_achetees, cout_actions_achetees,benefices = class_optimisation_force_brutee.optimis_force_brute(liste_new,0,1,2,500)
    print(str_liste_actions_achetees)
    print(cout_actions_achetees)
    print(benefices)

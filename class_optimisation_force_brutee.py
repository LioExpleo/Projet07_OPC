
from class_fonctions_generales import complete_chaine_car
#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float

class ClassOptimisForceBrute:
    # définition des attributs d'instance
    def __init__(self, liste_objet, nom_objet_position_liste, poids_objet_position_liste, valeur_objet_position_liste, poids_maxi):
        self.liste_objet = liste_objet
        self.nom_objet_position_liste = nom_objet_position_liste
        self.poids_objet_position_liste = poids_objet_position_liste
        self.valeur_objet_position_liste = valeur_objet_position_liste
        self.poids_maxi = poids_maxi

def optimis_force_brute(liste_objet, position_liste_nom_objet, position_liste_poids_objet, position_liste_valeur_objet, poids_maxi):
    long_liste = len(liste_objet)
    print("longueur de la liste des objets " + str(long_liste))
    length = 2 ** long_liste
    print("longueur de la boucle : 2 ** longueur de la liste " + str(length))
    print()

    #initialisation des données
    index = 0
    cout_total = 0
    valeure_totale = 0.0

    #La premiere boucle est effectuée (2 puissance nombre elements dans la liste
    # si 20 éléments dans la liste, s puissance 20 = 1 048 576 fois
    while index < length:
        # On récupère l'index pour le transformer en chaine de caractere en format bin
        # A chaque tour on incrémente la combinaison qui commence à 00000000000000000001
        # et se termine a 11111111111111111111
        # le caractere 0 correspondant à un ordre de ne pas acheter, alors que le 1 corresppond à acheter
        index_bin = (format(index, 'b'))
        str_index_bin = str(index_bin)

        #on remplace les caractere manquants par des 0 dans la chaine de caractere si le nombre binaire
        #dans la chaine de caractere est inferieur a la longueur de la liste
        #optimis : suppression des caracteres en plus de str_index_bin, et modification de la valeur de l'index au
        #depart pour aller chercher les bonnes valeurs
        #str_index_bin = complete_chaine_car(str_index_bin, long_liste, "0")
        #recuperation de la longueur de la liste de la chaine de caractere = long de la liste
        long_str_index_bin = len(str_index_bin)

        # index permettant d'aller chercher chaque caractere dans la chaine qui s'incrémente
        #index_str_index_bin = 0
        index_str_index_bin = long_liste - long_str_index_bin + 1

        cout = 0
        benef = 0.0
        #Pour toutes les actions (20 dans notre cas),
        # on regarde si 1 acheter, si c'est le cas, on rajoute le cout et le benefice au total
        while (index_str_index_bin < long_str_index_bin and cout <= poids_maxi):
            if (str_index_bin[index_str_index_bin] == '1'):
                cout = (cout + liste_objet[index_str_index_bin][position_liste_poids_objet])
                benef = (benef + (liste_objet[index_str_index_bin][position_liste_valeur_objet]))

            # si le bénéfice calculé est supérieur au benéfice calculé précedemment, on
            # écrase l'ancienne valeur, sinon on reboucle pour recalculer le bénéfice avec la combinaison suivante
            if valeure_totale < benef and cout <= poids_maxi:  # and cout <= 500
                valeure_totale = benef
                cout_total = cout
                #on complete la chaine str_index_bin si necessaire
                str_index_bin = complete_chaine_car(str_index_bin, long_liste, "0")
                liste_objets_select = str_index_bin
                #print(liste_objets_select)
            index_str_index_bin = index_str_index_bin + 1
        index = index + 1

    #liste des objets à sélectionner ou pas pour obtenir le meilleur benefice
    str_liste_objets_select = str(liste_objets_select)
    return str_liste_objets_select, cout_total, valeure_totale
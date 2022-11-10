import class_fonctions_generales
import class_optimisation_force_brute
import time
from class_fonctions_generales import complete_chaine_car, calcul_rapport_cout_gain
from operator import itemgetter
#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float
from class_optimisation_force_brute import optimis_force_brute

class ClassAlgoNew1:
    # définition des attributs d'instance
    def __init__(self, liste_objet, nom_objet_position_liste, poids_objet_position_liste, valeur_objet_position_liste, poids_maxi):
        self.liste_objet = liste_objet
        self.nom_objet_position_liste = nom_objet_position_liste
        self.poids_objet_position_liste = poids_objet_position_liste
        self.valeur_objet_position_liste = valeur_objet_position_liste
        self.poids_maxi = poids_maxi

# Solution optimale - programmation dynamique
#liste_triee_odre_cout = (sorted(new_list, key=itemgetter(1), reverse=True))
#print(liste_liste_triee_odre_cout)

def sacADos_dynamique(capacite, liste):
    # Solution optimale - programmation dynamique
    liste_triee = (sorted(liste, key=itemgetter(1), reverse = False))

    #print("liste triee du plus petit poids au plus grand pour construction matrice")
    #print(liste_triee)
    nbre_boucle = 0
    #Creation de la matrice allant de capacité 0 à capacité maximale et
    # pour une liste d'objet allant de 0 objet à toute la liste
    # pour tous les poids + colonne sans poids
    # et pour tous les objets + ligne sans objet
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(liste_triee) + 1)]

    for i in range(1, len(liste_triee) + 1): # pour toute la liste allant de la l
        #print(len(liste_triee))
        nbre_boucle += 1
        for w in range(1, capacite + 1):
            #print(capacite + 1)
            #print(int(liste_triee[i-1][1]))
            #print (w)
            nbre_boucle += 1

            if int(liste_triee[i-1][1]) <= w: #si le poids de la donnée traitée est inférieur au poids de la donnée traitée(colonne)
                #
                matrice[i][w] = max(liste_triee[i-1][2] + matrice[i-1][w-liste_triee[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    #print("nombre de boucle pour insérer les valeurs dans la matrice : " + str(nbre_boucle))
    #print(matrice)
    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(liste_triee)
    elements_selection = []

    #test de tous les élements de la liste
    while w >= 0 and n >= 0:
        nbre_boucle += 1
        e = liste_triee[n-1]

        # si matrice
        #print("n" + str(n))
        #print("w" + str(w))
        #print("e[1]" + str(e[1]))
        #print("e[2]" + str(e[2]))

        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            #print("elements_selection")
            #print(elements_selection)
            w -= e[1] #soustraire au poids maxi le poids de l'element selectionne
        n -= 1
    #print("nombre de boucle pour insérer les valeurs dans la matrice et rechercher les 20 éléments s'ils sont sélectionnés : " + str(nbre_boucle))
    #print(elements_selection)

    #Resultat de la matrice correspond à la derniere case, donc [-1][-1}
    return matrice[-1][-1], elements_selection

# Nom
# poids
# Valeur

#print('Algo dynamique', sacADos_dynamique(500, liste_triee))



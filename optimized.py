import class_algo_glouton
#import class_algo_new1
import class_sac_a_dos_dyn
import class_force_brute
import class_optimisation_force_brute
from class_script_csv import trsf_csv_list, trsf_csv_list_pds_int, trsf_csv_list_pds_int_p3
#from calcul import calcul_gain, calcul_cout
from operator import itemgetter
#from class_force_brute import force_brute
#from class_optimisation_force_brutee import optimis_force_brute
#import pandas as pandas
import time
from class_fonctions_generales import complete_chaine_car, factorielle, print_liste_objet, calcul_rapport_cout_gain
#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float
liste_donnees_1 = []
fichier_csv = 'Csv/Donnees_01.csv'
liste_donnees = trsf_csv_list(fichier_csv, liste_donnees_1)

#print("liste des donnees sans premiere ligne avec les nombres en float plutôt que char pour traitement")
#print(liste_donnees)
print()
liste_donnees_non_triees = liste_donnees #

print("***************************** ALGO SAS A DOS DYNAMIQUE FICHIER DE 20 ACTIONS *****************************")
print("Le prix des actions étant en € sans décimale, Big-O = nbre objet * capacité = 20 * 500 = 10 000")
debut_time_algo = time.time()
liste_donnees_2 =[]
fichier_csv = 'Csv/Donnees_01.csv'
liste_donnees = trsf_csv_list_pds_int(fichier_csv, liste_donnees_2)
#On maximalise par paquets de plus en plus grands, et à chaque fois qu'on trouve une maximalisation
# avec un nouvel élément,
#on maximalise avec le poids restant en récupérant la maximalisation précédente correspondant au poids restant,
#Principe de
benefice, liste_actions = class_sac_a_dos_dyn.sacADos_dynamique(500, liste_donnees )
print()
fin_time_algo = time.time()
temps_algo = fin_time_algo - debut_time_algo
print(str(temps_algo) + " secondes pour l'algorithme algo_new2 fichier de 20 actions ")

print("listes des actions pour le meilleur bénéfice avec un algorithme optimisé")
index = 0
for i in liste_actions:
    print(liste_actions[index][0])
    index += 1

index = 0
cout = 0
for i in liste_actions:
    cout = cout + liste_actions[index][1]
    index += 1

print("pour un coût de  : " + str(cout) + "€" + " et un benefice de " + str(benefice) + "€")
print()

print()
print("***************************** ALGO SAS A DOS DYNAMIQUE 1er FICHIER SIENNA *****************************")


#*calcul bénéfices données 1 partie 3 du projet******************************************
debut_time_algo = time.time()
liste_donnees_2 =[]

fichier_csv = 'Csv/P3_Donnees01.csv'

liste_donnees = trsf_csv_list_pds_int_p3(fichier_csv, liste_donnees_2)
print("nombre de donnees après avoir supprimé les erreurs : " + str (len(liste_donnees)))
print("Le prix des actions étant en € avec décimales, Big-O = nbre objet * capacité * 100 = 957 * (500 * 100) = 47 850 000")

##Remplacement du poucentage de gain par le gain en centimes d'euros dans la liste
index = 0
for i in liste_donnees:
    liste_donnees [index][2] = liste_donnees [index][1] * liste_donnees [index][2] /100 /100
    index += 1

#On maximalise par paquets de plus en plus grands, et à chaque fois qu'on trouve une maximalisation avec un nouvel élément,
#on maximalise avec le poids restant en récupérant la maximalisation précédente correspondant au poids restant,
#Principe de

benefice, liste_actions = class_sac_a_dos_dyn.sacADos_dynamique(50000, liste_donnees )
print()

fin_time_algo = time.time()
temps_algo = fin_time_algo - debut_time_algo
print(str(temps_algo) + " secondes pour l'algorithme algorithme optimisé avec le 1er fichier SIENNA ")

print("listes des actions pour le meilleur bénéfice avec un algorithme optimisé")
index = 0
for i in liste_actions:
    print(liste_actions[index][0])
    index += 1

#Calcul du cout total des actions
index = 0
cout = 0
for i in liste_actions:
    cout = cout + liste_actions[index][1]
    index += 1

cout = cout / 100
print("pour un coût de  : " + str(cout) + "€" + " et un benefice de " + str(round(benefice, 2)) + "€")
print()
print()
print("***************************** ALGO SAS A DOS DYNAMIQUE 2ème FICHIER SIENNA *****************************")
#*calcul bénéfices données 2 partie 3 du projet*****************************************************
debut_time_algo = time.time()
liste_donnees_2 =[]
fichier_csv = 'Csv/P3_Donnees02.csv'
liste_donnees = trsf_csv_list_pds_int_p3(fichier_csv, liste_donnees_2)
print("nombre de donnees après avoir supprimé les erreurs : " + str (len(liste_donnees)))
print("Le prix des actions étant en € avec décimales, Big-O = nbre objet * capacité * 100 = 541 * (500 * 100) = 27 050 000")

##Remplacement du poucentage de gain par le gain en centimes d'euros dans la liste
index = 0
for i in liste_donnees:
    liste_donnees [index][2] = liste_donnees [index][1] * liste_donnees [index][2] /100 /100
    index += 1

#On maximalise par paquets de plus en plus grands, et à chaque fois qu'on trouve une maximalisation avec un nouvel élément,
#on maximalise avec le poids restant en récupérant la maximalisation précédente correspondant au poids restant,
#Principe de

benefice, liste_actions = class_sac_a_dos_dyn.sacADos_dynamique(50000, liste_donnees )
print()

fin_time_algo = time.time()
temps_algo = fin_time_algo - debut_time_algo
print(str(temps_algo) + " secondes pour l'algorithme algorithme optimisé avec le 2eme fichier SIENNA ")

print("listes des actions pour le meilleur bénéfice avec un algorithme optimisé")
index = 0
for i in liste_actions:
    print(liste_actions[index][0])
    index += 1

#Calcul du cout total des actions
index = 0
cout = 0
for i in liste_actions:
    cout = cout + liste_actions[index][1]
    index += 1

cout = cout / 100
print("pour un coût de  : " + str(cout) + "€" + " et un benefice de " + str(round(benefice, 2)) + "€")

print()








#print(liste_actions)
"""

# Demande à l'utilisateur d'entrer un nombre
#n = int(input("Entrez un nombre pour calcul factorielle: "))
#print("factorielle de " + str(n) + " = " + str(factorielle(n)))
"""



"""
"""
"""
def recursive(n, index):
    if n == 0:
        return(n)
    else:
        for i in liste_achat:
            index = index +2
            1
            print(index)

        return (recursive(n-1, index))
recursive(n,0)
print("*******fin recursive*********")
"""
"""
mdp=''
print("****************")
print(liste_achat)
def bruteforce(liste, word,length):
    index_print = 0
    #if length <= 1 :
    test_recursiv = 0
    #n = longueur de la liste
    #pour faire une fonction récursive 20 fois
    def recursive(n):
        if n == 0:
            return("fin")
        else:

            for i in liste_achat:
                print(length)
                # length = length + 1
                test_recursiv = test_recursiv + 1
                print(test_recursiv)
            recursive(recursive(n-1))


    for i in liste_achat:
        print(length)
        #length = length + 1

        for i in liste_achat:
            print(length)
            #length = length + 1

            for i in liste_achat:
                print(length)
                #length = length + 1

                for i in liste_achat:
                    print(length)

                    for i in liste_achat:
                        print(length)

                        for i in liste_achat:
                            print(length)

                            for i in liste_achat:
                                print(length)
                                for i in liste_achat:
                                    print(length)
                                    for i in liste_achat:
                                        print(length)
                                        for i in liste_achat:
                                            print(length)
                                            for i in liste_achat:
                                                print(length)
                                                for i in liste_achat:
                                                    print(length)
                                                    for i in liste_achat:
                                                        print(length)

                                                        for i in liste_achat:
                                                            print(length)

                                                            for i in liste_achat:
                                                                print(length)

                                                                for i in liste_achat:
                                                                    print(length)

                                                                    for i in liste_achat:
                                                                        print(length)

                                                                        for i in liste_achat:
                                                                            print(length)

                                                                            for i in liste_achat:
                                                                                print(length)

                                                                                for i in liste_achat:
                                                                                    print(length)
                                                                                    length = length + 1


mdp = input("entrez votre nombre : ")
bruteforce(liste_achat,'',0 )

print("****************")
"""

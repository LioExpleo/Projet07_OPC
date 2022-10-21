import class_algo_glouton
import class_force_brute
import class_optimisation_force_brutee
from class_script_csv import trsf_csv_list
from calcul import calcul_gain, calcul_cout
from operator import itemgetter
from class_force_brute import force_brute
from class_optimisation_force_brutee import optimis_force_brute
import pandas as pandas
import time
from class_fonctions_generales import complete_chaine_car, factorielle, print_liste_objet, calcul_rapport_cout_gain

#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float
liste_donnees_1 = []
fichier_csv = 'Csv/Donnees_01.csv'
liste_donnees = trsf_csv_list(fichier_csv, liste_donnees_1)

print("liste des donnees sans premiere ligne avec les nombres en float plutôt que char pour traitement")
print(liste_donnees)
print()
liste_donnees_non_triees = liste_donnees

#pour que lors des tests, on sorte de la boucle si le budget restant est inférieur
# au prix de la prochaine action, on met les actions dans l'ordre de prix croissant

#print("mise des actions dans l'ordre de leurs prix croissant ")
#print(sorted(liste_donnees, key = itemgetter(1), reverse=False))

#budget pour achat des actions 500€
budget_total = 500
cout_action_acht = 0
budget_restant = budget_total - cout_action_acht
debut_time_algo = time.time()
str_liste_actions_achetees, cout_actions_achetees,benefices=class_force_brute.force_brute(liste_donnees_non_triees,0,1,2,500)
fin_time_algo = time.time()
temps_algo = fin_time_algo - debut_time_algo

print("FORCE BRUTE")
print(str(temps_algo) + " secondes pour l'algorithme force brute")
print("format binaire de représentation de la liste des actions achetees pour avoir le meilleur bénéfice avec force brute: " + str_liste_actions_achetees)
long_liste = len(str_liste_actions_achetees)

#print liste actions
print_liste_objet(liste_donnees,str_liste_actions_achetees,0)
print("cout total des actions achetees : " + str("%.2f" % cout_actions_achetees) + "€")
print("bénéfices sur les actions achetees : " + str(round(benefices,2)) + "€")
print()
print()

print("OPTIMISATION")
print ("liste_donnees_triees pour 2ème partie de programme")
liste_donnees_triees = sorted(liste_donnees, key = itemgetter(1), reverse=False)
#length est la longueur recuperee de la liste (20)
long_list = len(liste_donnees_triees)
print(long_list)
print (liste_donnees_triees)

debut_time_algo = time.time()
str_liste_actions_achetees, cout_actions_achetees,benefices = class_optimisation_force_brutee.optimis_force_brute(liste_donnees_triees,0,1,2,500)
fin_time_algo = time.time()
temps_algo = fin_time_algo - debut_time_algo
#print liste actions
print(str(temps_algo) + " secondes pour l'algorithme optimisation force brute")

print_liste_objet(liste_donnees_triees,str_liste_actions_achetees,0)
print("cout total des actions achetees : " + str("%.2f" % cout_actions_achetees) + "€")
print("bénéfices sur les actions achetees : " + str(round(benefices,2)) + "€")
print()
print()


#Algo optimisé V2 Rappport_benef_masse = benefice/masse
#new_list = calcul_rapport_cout_gain(liste_donnees_non_triees)
#print(new_list)




class_algo_glouton.algo_glouton(liste_donnees_non_triees,0,1,2,500)






print()
print()
# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre pour calcul factorielle: "))
print("factorielle de " + str(n) + " = " + str(factorielle(n)))
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

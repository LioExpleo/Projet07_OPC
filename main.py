import class_force_brute
from class_script_csv import trsf_csv_list
from calcul import calcul_gain, calcul_cout
from operator import itemgetter
from class_force_brute import force_brute
import pandas as pandas
import time
from class_fonctions_generales import complete_chaine_car, factorielle, print_liste_objet

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

str_liste_actions_achetees, cout_actions_achetees,benefices=class_force_brute.force_brute(liste_donnees_non_triees,0,1,2,500)
print("format binaire de représentation de la liste des actions achetees pour avoir le meilleur bénéfice: " + str_liste_actions_achetees)
long_liste = len(str_liste_actions_achetees)

#print liste actions
print_liste_objet(liste_donnees,str_liste_actions_achetees,0)
print("cout total des actions achetees : " + str("%.2f" % cout_actions_achetees) + "€")
print("bénéfices sur les actions achetees : " + str(round(benefices,2)) + "€")







print ("liste_donnees_triees pour 2ème partie de programme")
liste_donnees_triees = sorted(liste_donnees, key = itemgetter(1), reverse=False)
#length est la longueur recuperee de la liste (20)
long_list = len(liste_donnees_triees)
print(long_list)
print (liste_donnees_triees)




# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre pour calcul factorielle: "))
print("factorielle de " + str(n) + " = " + str(factorielle(n)))
"""
def bruteforce(liste_objet, position_liste_nom_objet, position_liste_poids_objet, position_liste_valeur_objet, poids_maxi):
    long_liste = len(liste_objet)
    print("longueur de la liste " + str(long_liste))
    length = 2 ** long_liste
    print("longueur de la boucle " + str(length))
    

    #init index de la boucle allant de 0 à length
    index = 0
    cout_total = 0
    benef_total = 0.0

    #La premiere boucle est effectuée (2 puissance nombre elements dans la liste
    # si 20 éléments dans la liste, s puissance 20 = 1 048 576 fois
    while index < length:
        # On récupère l'index pour le transformer en chaine de caractere en format bin
        # A chaque tour on incrémente la combinaison qui commence à 00000000000000000001
        # et se termine a 11111111111111111111
        # 0 correspondant à ne pas acheter, et 1 à acheter
        index_bin = (format(index, 'b'))
        str_index_bin = str(index_bin)

        #on remplace les caractere manquants par des 0 dans la chaine de caractere si le nombre binaire
        #dans la chaine de caractere est inferieur a la longueur de la liste
        str_index_bin = complete_chaine_car(str_index_bin, long_liste, "0")

        #recuperation de la longueur de la liste de la chaine de caractere
        long_str_index_bin = len(str_index_bin)

        # index permettant d'aller chercher chaque caractere dans la chaine qui s'incrémente
        index_str_index_bin = 0

        cout = 0
        benef = 0.0
        #Pour toutes les actions (20 dans notre cas),
        # on regarde si 1 acheter, si c'est le cas, on rajoute le cout et le benefice au total
        while (index_str_index_bin < long_str_index_bin):
            if (str_index_bin[index_str_index_bin] == '1'):
                cout = (cout + liste_objet[index_str_index_bin][position_liste_poids_objet])
                benef = (benef + (liste_objet[index_str_index_bin][position_liste_valeur_objet]))

            # si le bénéfice calculé est supérieur au benéfice calculé précedemment, on
            # écrase l'ancienne valeur, sinon on reboucle pour recalculer le bénéfice avec la combinaison suivante
            if benef_total < benef and cout <= 500:  # and cout <= 500
                benef_total = benef
                cout_total = cout
                liste_action_achetees = str_index_bin
                #print(liste_action_achetees)
            index_str_index_bin = index_str_index_bin + 1
        index = index + 1

    print("Meilleur bénefices obtenus avec cette liste actions achetees ")
    str_liste_action_achetees = str(liste_action_achetees)
    print(str_liste_action_achetees)

    index_aa = 0
    print("liste des achats pour le meilleur benefice : ")
    #parcourir la liste des 20 actions
    while index_aa < long_liste:
        # Dans la chaine de caractere, afficher l'action, où si indiqué actions à acheter par "1"
        if (str_liste_action_achetees[index_aa] == '1'):
            print (liste_objet[index_aa][position_liste_nom_objet])
        index_aa = index_aa + 1

    print("cout total : " + str("%.2f" % cout_total) + "€")
    print("benefice total : " + str(round(benef_total,2)) + "€")

bruteforce(liste_donnees_non_triees,0,1,2,500)
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

from Script_csv import trsf_csv_list
from calcul import calcul_gain, calcul_cout
from operator import itemgetter
import pandas as pandas
import time


fichier_csv = 'Csv/Donnees_01.csv'

#recupération dans une liste des donnees avec suppression de la 1ere ligne pour n'avoir
# que des donnees, et suppression des guillemets pour avoir des float
liste_donnees_1 = []
liste_donnees = trsf_csv_list(fichier_csv, liste_donnees_1)
print("liste des donnees sans premiere ligne avec les nombres en float plutôt que char pour traitement")
print(liste_donnees)
print()
liste_donnees_non_triees = liste_donnees
#pour que lors des tests, on sorte de la boucle si le budget restant est inférieur
# au prix de la prochaine action, on met les actions dans l'ordre de prix croissant
print("mise des actions dans l'ordre de leurs prix croissant ")
print(sorted(liste_donnees, key = itemgetter(1), reverse=False))
liste_donnees_triees = sorted(liste_donnees, key = itemgetter(1), reverse=False)
print (liste_donnees_triees)


#budget pour achat des actions 500€
budget_total = 500
cout_action_acht = 0
budget_restant = budget_total - cout_action_acht

#length est la longueur recuperee de la liste (20)
long_list = len(liste_donnees_triees)
print(long_list)

def factorielle(n):
    """Ceci est une fonction récursive qui appelle
   lui-même pour trouver la factorielle du nombre donné"""
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)
# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre pour calcul factorielle: "))
print("factorielle de " + str(n) + " = " + str(factorielle(n)))
"""
liste = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
n = int(input("Entrez un nombre pour test fonction recursivite: "))

#calcul de la récursivité
n = len(liste)
n = 2 ** 4
print("recursivite")
print(n)
"""

def bruteforce(liste):
    long_liste = len(liste)
    print("longueur de la liste " + str(long_liste))
    length = 2 ** long_liste
    print("longueur de la boucle " + str(length))
    index = 0
    cout_total = 0
    benef_total = 0.0

    #La premiere boucle est effectuée (2 puissance nombre elements dans la liste
    # si 20 éléments dans la liste, s puissance 20 = 1 048 576 fois
    while index < length:
        #print(index)
        index_bin = (format(index, 'b'))

        # A chaque tour on incrémente la combinaison qui commence à 00000000000000001
        # et se termine a                                           11111111111111111

        # chaque bit de index_bin correspond à acheter si = 1 et ne pas acheter si = 0
        # on récupère le nombre binaire dans une chaine de caractere
        # pour toute la liste, si le bit = 1, on achete, si 0 on passe
        #for i in liste ou  tant que toute la liste n'est pas scrutée
        # on passe à l'objet de la liste suivant

        #recuperation du nombre en binaire dans une chaine de caractere afin d'aller chercher
        #chaque élement 1 ou 0

        str_index_bin = str(index_bin)

        #nombre de caractere dans la chaine, au départ moins de 20, donc pas la peine de faire 20 tours dans la boucle
        # les 20 apparaissent à partir de la fin
        #print("longueur de le liste")
        #print (long_str_index_bin)
        #boucle qui va cherhcer les donnees si 1, et laisse si 0
        #****************************************************
        # POUR TEST DE LA SUITE, ACHAT DE TOUTES LES ACTIONS
        #str_index_bin = "00111"
        long_str_index_bin = 3

        #****************************************************
        long_str_index_bin = len(str_index_bin)
        # index permettant d'aller chercher chaque caractere dans la chaine
        index_str_index_bin = 0
        cout = 0
        benef = 0.0

        while (index_str_index_bin < long_str_index_bin):
            # il faudra appeler ici, le calcul du cout et des benefices
            # print (str_index_bin[index_str_index_bin])
            # si le bit correspondant au numero de l'action = 1, achat, sinon rien

            if (str_index_bin[index_str_index_bin] == '1'):
                #print("str_index_bin[index_str_index_bin]")
                #print(str_index_bin[index_str_index_bin])
                #print()
                #cout = (cout + liste_donnees_triees[index_str_index_bin][1])
                cout = (cout + liste[index_str_index_bin][1])
                #print (cout)
                #benef = (benef + liste_donnees_triees[index_str_index_bin][2])
                benef = (benef + float(liste[index_str_index_bin][2]))
                    #print(cout)
                    #print (benef)
                    #print(index_str_index_bin)

                if (float(benef_total) < float(benef) and cout <= 500.0):  # and cout <= 500
                    benef_total = benef
                    print (benef_total)
                    cout_total = cout
                    #liste_action_achetees = index
                    #index_bin = (format(index, 'b'))
                    liste_action_achetees = (format(index, 'b'))

            index_str_index_bin = index_str_index_bin + 1
        index = index + 1

    print("Meilleur bénefices obtenus avec cette liste actions achetees ")
    print(liste_action_achetees)
    index_aa = 0
    print("liste des achats pour le meilleur benefice : ")
    while index_aa < long_str_index_bin:
        if (liste_action_achetees[index_aa] == '1'):
            print(liste[index_aa][0])
        index_aa = index_aa + 1

    print("cout total : " + str(cout_total) + "€")
    #print(cout_total)
    print("benefice total : " + str(benef_total) + "€")
    # ici, aller chercher la liste des actions, permet de ne le faire qu'une fois le résultat total obtenu


        #pour les 20 actions, on regarde se le bit = 0, si bit = 0, on ajoute pas le cout au cout, sinon on l'ajoute
        #idem pour le benefice, ensuite, on range tout dans une liste avec append


bruteforce(liste_donnees_non_triees)


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
"""


"""
"""


"""
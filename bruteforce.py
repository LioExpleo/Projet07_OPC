import class_algo_glouton
#import class_algo_new1
import class_sac_a_dos_dyn
import class_force_brute
import class_optimisation_force_brute
from class_script_csv import trsf_csv_list, trsf_csv_list_pds_int, trsf_csv_list_pds_int_p3
from operator import itemgetter
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

print("********************************************FORCE BRUTE********************************************")
print(str(temps_algo) + " secondes pour l'algorithme force brute")
print("format binaire de représentation de la liste des actions achetees pour avoir le meilleur bénéfice avec force brute: " + str_liste_actions_achetees)
long_liste = len(str_liste_actions_achetees)

#print liste actions
print_liste_objet(liste_donnees,str_liste_actions_achetees,0)
print("cout total des actions achetees : " + str("%.2f" % cout_actions_achetees) + "€")
print("bénéfices sur les actions achetees : " + str(round(benefices,2)) + "€")
print()

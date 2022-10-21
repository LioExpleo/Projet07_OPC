import csv
import time

class ClassMethodesCsv:
    # définition des attributs d'instance
    def __init__(self, NameCsv, ListeTotale,encodage,liste):
        self.NameCsv = NameCsv
        self.ListeTotale = ListeTotale
        self.encodage = encodage
        self.liste = liste

def WriteCsv(NameCsv,ListeTotale,encodage):
# Fonction qui écrit un fichier csv à partir d'une liste, l'encodage étant à préciser
# ouverture du fichier excel en écriture
    with open(NameCsv, 'w', encoding=str(encodage), newline="") as myFile2:  # ,encoding='utf-8'#sig indique a excel que utf-8 est utilisé pour l'encodage
        writer = csv.writer(myFile2,delimiter=";")  # Ecriture dans le fichier excel Avec la virgule pour séparer les champs
        LenListeTotale = ListeTotale.__len__()  # #récupération de la longueur de la liste de liste, la liste commençant à 0
        #print("longueur de la liste avant writer.writerow " + str(LenListeTotale))
        for iListe in ListeTotale:  # Ecrire la totalité des listes de listes dans le fichier excel
            writer.writerow(iListe)

def trsf_csv_list(NameCsv, liste):
    # Ouvrir le fichier csv
    with open(NameCsv, 'r') as f:
        # Créer un objet csv à partir du fichier
        index_list = 0;
        obj = csv.reader(f)
        for ligne in obj:
            liste.append(ligne)
        #supprimer la 1ere ligne de la liste qui ne peut être traitée
        liste.pop(0)

        long_list = len(liste)
        index_list = 0

        while (index_list < (long_list)):
            liste[index_list][1] = float(liste[index_list][1])
            liste[index_list][2] = float(liste[index_list][2])
            index_list = index_list + 1
    return liste


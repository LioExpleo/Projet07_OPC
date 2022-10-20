
class ClassFonctionsGenerales:
    # définition des attributs d'instance
    def __init__(self, chaine_char, long_a_atteindre, char_complete_chaine, n):
        self.chaine_char = chaine_char
        self.long_a_atteindre = long_a_atteindre
        self.char_complete_chaine = char_complete_chaine
        self.n = n

def complete_chaine_car(chaine_char,long_a_atteindre, char_complete_chaine):
    long_liste = len(chaine_char)
    while long_liste < long_a_atteindre:
        chaine_char = char_complete_chaine + chaine_char
        long_liste = len(chaine_char)
    return chaine_char

def factorielle(n):
    """Ceci est une fonction récursive qui appelle
   lui-même pour trouver la factorielle du nombre donné"""
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)

def print_liste_objet(liste, str_liste_select_1_0, position_liste_nom_objet):
    index_aa = 0
    long_liste = len(str_liste_select_1_0)
    while index_aa < long_liste:
        # Dans la chaine de caractere, afficher l'action, où si indiqué actions à acheter par "1"
        if (str_liste_select_1_0[index_aa] == '1'):
            print(liste[index_aa][position_liste_nom_objet])
        index_aa = index_aa + 1
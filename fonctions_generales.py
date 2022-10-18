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
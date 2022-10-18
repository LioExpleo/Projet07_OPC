import time
def calcul_cout(liste_action, liste_select_action):
    index_bcl = 0
    cout_total = 0
    for i in liste_select_action:
        time.sleep(0.01)
        index_action = liste_select_action[index_bcl]
        cout_total = cout_total + int(liste_action[index_action][1])
        index_bcl = index_bcl + 1
        #print(cout_total)
    return cout_total

def calcul_gain(liste_action, liste_select_action):
    index_bcl = 0
    gain_total = 0
    for i in liste_select_action:
        time.sleep(0.01)
        index_action = liste_select_action[index_bcl]
        gain_total = gain_total + float(liste_action[index_action][2])
        index_bcl = index_bcl + 1
    return gain_total
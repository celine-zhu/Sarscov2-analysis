#L est une liste de séquences, les séquences étant des listes de chaînes de caractère, chaque chaîne de caractère correspondant à un acide aminé
#aa est une chaîne de caractère correspondant à un acide aminé
def var_aa(L,aa):
    l = len(L)

    #Pour éviter de diviser par zéro par la suite
    if l == 0 :
        return 0

    #Liste qui contient de le nombre de fois qu'il y a aa dans chaque séquence
    Nb_aa = [0]*l
    for i in range(l):
        for string in L[i] :
            if string == aa :
                Nb_aa[i] += 1

    esp = sum(Nb_aa)/l

    esp2 = 0
    for nb in Nb_aa :
        esp2 += nb**2
    esp2 = esp2/l

    #Théorème de Keonig-Huygens
    return esp2 - (esp**2)
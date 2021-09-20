def mediane_aa(L):
#L une liste de séquences et chaque séquence est une liste de chaines de caractères, chacune correspondant à un acide aminé
    n = len(L)
    M = []

    if n == 0:          #Pour éliminer le cas particulier d'une liste vide
        return 0

    for i in range(0,n):
        for j in range (0,len(L[i])):
            M.append(len(L[i][j]))
    #Liste qui contient de le nombre de chaines de caractères de chaque acide animé

    k = len(M)
    M = sorted(M)     #classer les éléments de la liste

    if k%2 == 0:          #Traiter le cas où le nombre de séquences est pair
        a = M(k//2)
        b = M((k//2)+1)
        return (a+b)/2
        #Retourner la demi-somme de deux nombres de caracères des deux acides aminés au milieu

    else:          #l'autre cas où le nombre de séquences est impair
        return M(k//2)
        #Retourner le nombre des acides aminés de la séquence au milieu



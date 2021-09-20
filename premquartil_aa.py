def premquartil_aa(L):
#L une liste de séquences et chaque séquence est une liste de chaines de caractères, chacune correspondant à un acide aminé
    n = len(L)
    Q = []

    if n == 0:          #Pour éliminer le cas particulier d'une liste vide
        return 0

    for i in range(0,n):
        for j in range (0,len(L[i])):
            Q.append(len(L[i][j]))
    #Liste qui contient de le nombre de chaines de caractères de chaque acide animé

    k = len(Q)
    Q = sorted(Q)     #classer les éléments de la liste

    if k%4 == 0:
        return Q([k//4]) #le premier quartile est la 0,25*k_ième valeur
    else:
        return Q([(k//4)+1])
        #le premier quartile est [0,25*k]+1_ième valeur


def var_leng(L):
    n = len(L) #calcul du nombre de sequences

    if n == 0:
        return 0

    M = []
    esp = 0
    esp2 = 0

    for j in range(0,n):
        M.append(len(L[j]))  #calcul du nombre de nucléotide dans une sequence

    esp = sum(M)/n    #la moyenne

    for i in range(0,n):
        esp2 += (M[i])**2

    esp2 = esp2/n             #la variance

    return esp2 - (esp**2)

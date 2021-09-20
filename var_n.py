def var_n(liste,n):  #on donne une liste de listes des sequences(list[list[char]])          
                     #et le nucléotide  dont on veut     
                     #calculer la variance du nombre d'occurences de n dans             
                     #l'ensemble des sequences (char)
    l=[]           #liste où chaque casse i = nombre de n dans sequence i
    for i in range(len(liste)):
        compteur=0
        for j in range(len(liste[i])):
            if liste[i][j]==n:
                compteur+=1
        l.append(compteur)
    #On calcule la moyenne
    compteur=0
    for i in range(len(l)):
        compteur+=l[i]
    moyenne=compteur/len(l)
    #On calcule variance
    compteur=0
    for i in range(len(l)):
        compteur+=(l[i]-moyenne)**2
    variance=compteur/len(l)
    return variance     #On retourne la variance de la quantité de nucléotides n 
                    # dans l'ensemble des séquences
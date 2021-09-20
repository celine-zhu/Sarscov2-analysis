from fas2ch import fas2ch

#annee et mois sont des entiers, et la fonction renvoie une liste de listes de caracteres

def date(annee,mois) :

    #verifie que la date demandee existe, si non la fonction retourne une liste vide (ne contenant pas de sequences)
    if annee != 2020 or mois < 1 or mois > 11 :
        return []

    #ecrit le mois en chaine de caractères afin de construire le nom du fichier
    if mois < 10 :
        mois_str = "0" + str(mois)
    else :
        mois_str = str(mois)

    #applique la fonction fas2ch au bon nom de fichier
    return fas2ch("Sequences_" + str(annee) + "_" + mois_str + ".fasta")
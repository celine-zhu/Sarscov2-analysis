from Bio import SeqIO


#le pays (chaine de caracteres) doit etre donne sous forme de l'abreviation à trois lettres definie par l'OTAN
#les mois1 et mois2 sont des entiers naturels, on ne va prendre en compte que les sequences prelevees entre ces deux mois (inclus)
#il faut mois1 <= mois2, ou la fonction retournera une liste vide
def geog(pays, mois1, mois2) :


    #Recherche du nom du pays dans une chaine de caractères
    def is_from(mot, phrase) :
        n = len(mot)
        for i in range(len(phrase)-n) :
            if phrase[i:i+n] == mot :
                return True
        return False


    #Liste qui va contenir les sequences cherchees
    L = []


    #parcourir tous les fichiers fasta, en faisant attention a ce que la variable mois prenne bien des valeurs qui correspondent à des fichiers fasta existants
    for mois in range(max(1, mois1), min(12, mois2 + 1)) :


        #ecrit le mois en chaine de caracteres pour construire le nom du fichier fasta correspondant
        if mois < 10 :
            mois_str = "0" + str(mois)
        else :
            mois_str = str(mois)

        #ajoute a L les sequences qui viennent du pays souhaite
        for seq_record in SeqIO.parse("Sequences_2020_" + mois_str + ".fasta","fasta") :

            if is_from("/" + pays + "/", seq_record.description) :
                L1 = []
                for k in seq_record.seq :
                    L1.append(k)
                L.append(L1)

    return L


def codons(seq):     #on prend une séquence d'ARNm sous forme de liste 
    L_codons=[]      # liste constituée de la séquence de codons associés 
    L_acides=[]      #liste constituée de la séquence d'acides aminés associés       
    start=[]
    N=int(len(seq)/3)+1
    
    tableau=[['F','TTT','TTC'],['L','TTA','TTG','CTT','CTC','CTA','CTG'],['I','ATT','ATC','ATA'],['M','ATG'],['V','GTT','GTC','GTA','GTG'],['S','TCT','TCC','TCA','TCG','AGT','AGC'],['P','CCT','CCC','CCA','CCG'],['T','ACT','ACC','ACA','ACG'],['A','GCT','GCC','GCA','GCG'],['Y','TAT','TAC'],['Stop ocre','TAA'],['Stop ambre','TAG'],['H','CAT','CAC'],['Q','CAA','CAG'],['N','AAT','AAC'],['K','AAA','AAG'],['D','GAT','GAC'],['E','GAA','GAG'],['C','TGT','TGC'],['Stop opale','TGA'],['W','TGG'],['R','CGT','CGC','CGA','CGG','AGA','AGG'],['G','GGT','GGC','GGA','GGG']]
    #tableau où dans chaque case i, i[0] représente un acide aminé et les i[j] (j!=0) les codons qui lui sont associés
      #si la longueur de la séquence n'est pas multiple de 3 (donc si elle n'est pas entièrement transformable en séquence d'acides aminés), on retourne une liste vide 
    seq=seq[:N]
    n=len(seq)-2
    for i in range(0,n,3): #on construit L_codons
            L_codons.append(seq[i]+seq[i+1]+seq[i+2])
            b=seq[i]+seq[i+1]+seq[i+2]
            if b=='ATG':
                start.append(i)
    if start==[]:
            return []
    for k  in range(start[0], len(L_codons)): #pour chaque codon ,on lui associe un acide aminé (on constuit L_acides)
            for acide in tableau:
                for c in range(1,len(acide)):
                    if L_codons[k]==acide[c]:
                        L_acides.append(acide[0])
                        if 'Stop' in acide[0]:
                            return L_acides
    return L_acides
                    
                    
    
    
    
    
    

    
    
 
    
                   
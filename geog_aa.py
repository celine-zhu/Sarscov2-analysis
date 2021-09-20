from geog import geog

def geog_aa(pays, mois1, mois2):
    liste=geog(pays, mois1, mois2)
    aa=[]
    for seq in liste:
        aa.append(codons(seq))
    return aa
    

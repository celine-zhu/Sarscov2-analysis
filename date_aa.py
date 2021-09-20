from date import date
from codons import codons

    
def date_aa(annee,mois):
    liste=date(annee,mois)
    aa=[]
    for seq in liste:
        aa.append(codons(seq))
    return aa

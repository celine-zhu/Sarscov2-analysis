import pytest
from date_aa import date_aa

#on vérifie la taille de la liste renvoyée
def test_date_aa1():
    assert len(date_aa(2020,1))==33

#cas où une des séquences de la liste en paramètre est bien multiple de trois (len(date(2020,1)[23])%3==0)
def test_date_aa2():
    assert date_aa(2020,1)[23][:15]==['I', 'K', 'G', 'L', 'Y', 'L', 'P', 'R', 'Stop ocre', 'Q', 'T', 'N', 'Q', 'L', 'S']
    
#cas où une des séquences de la liste en paramètre n'est pas multiple de trois (len(date(2020,1)[1])%3==2)   
def test_date_aa3():
    assert date_aa(2020,1)[1]==[]
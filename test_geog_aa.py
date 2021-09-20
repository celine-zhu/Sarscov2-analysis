from timeit import timeit
from geog import geog
from codons import codons
from geog_aa import geog_aa

#Tester ce qu'il se passe si le pays en paramètre n'existe pas
def test_geog_aa1() :
    assert geog_aa("AAA",1,2) == []

#Tester ce qu'il se passe si mois1 est trop petit
def test_geog_aa2() :
    assert geog_aa("USA",0,2) == codons(geog("USA",1,2))

#Tester ce qu'il se passe si mois2 est trop grand
def test_geog_aa3() :
    assert geog_aa("USA",10,13) == codons(geog("USA",10,11))

#Tester ce qu'il se passe si mois1 > mois2
def test_geog_aa4() :
    assert geog_aa("USA",2,1) == []

#Verifier que si mois1 = mois2, alors on a quand meme les sequences du mois correspondant
def test_geog_aa5() :
    assert geog_aa("USA",1,1) == codons(geog("USA",1,1))

#Test temporel
def test_time_geog_aa() :
    s = 0
    for mois in range(1,5) :
        s += len(date(2020,mois))
    assert timeit.timeit(lambda:"geog_aa(\"USA\",1,4)", number=1) < s*30000/(10**9)

import pytest
import timeit
from geog import geog
from date import date

#Tester ce qu'il se passe si le pays en paramètre n'existe pas
def test_geog1() :
    assert geog("AAA",1,2) == []

#Tester ce qu'il se passe si mois1 est trop petit
def test_geog2() :
    assert geog("USA",0,2) == geog("USA",1,2)

#Tester ce qu'il se passe si mois2 est trop grand
def test_geog3() :
    assert geog("USA",10,13) == geog("USA",10,11)

#Tester ce qu'il se passe si mois1 > mois2
def test_geog4() :
    assert geog("USA",2,1) == []

#Verifier que si mois1 = mois2, alors on a quand meme les sequences du mois correspondant
def test_geog5() :
    assert geog("USA",1,1) != []

#Test temporel
def test_geog6() :
    s = 0
    for mois in range(1,5) :
        s += len(date(2020,mois))
    assert timeit.timeit(lambda:"geog(\"USA\",1,4)", number=10)/10 < s*30000/(10**9)

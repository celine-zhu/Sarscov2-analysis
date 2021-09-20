import pytest
import timeit
from needwu import needwu
from date import date
from random import randint

#Le mois d'avril contient plus de mille séquences, ce qui représente un échantillon assez important
L = date(2020,4)
n = len(L)
S = [[10,-1,-3,-4],[-1,7,-5,-3],[-3,-5,9,0],[-4,-3,0,8]]
d = -5


"""Test Boundary"""

#Vérifie que si les séquences sont identiques, l'alignement retourné laisse les séquences telles quelles
def test_needwu1() :
    i = randint(0, n-1)
    Li = L[i][:1000]
    align = ""
    for char in Li :
        align += char
    assert needwu(Li,Li,S,d) == align, align

"""Test Performance"""

#Test temporel
def test_needwu2() :
    i = randint(0, n-1)
    Li = L[i][:1000]
    j = randint(0, n-1)
    Lj = L[j][:1000]
    assert timeit.timeit(lambda:"needwu(Li,Lj,S,d", number=10)/10 <= len(Li)*len(Lj)/(10**9)
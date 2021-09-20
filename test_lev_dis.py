import pytest
import timeit
from lev_dis import lev_dis
from date import date
from random import randint

#Le mois d'avril contient plus de mille séquences, ce qui représente un échantillon assez important
L = date(2020,4)
n = len(L)


"""Test Right"""

#Vérifie que la distance de levenshtein reste la meme si l'on inverse les paramètres
def test_lev_dis1() :
    i = randint(0, n-1)
    j = randint(0, n-1)
    assert lev_dis(L[i][:1000], L[j][:1000]) == lev_dis(L[j][:1000], L[i][:1000])

"""Test Boundary"""

#Vérifie que si les séquences sont identiques, la fonction retourne 0
def test_lev_dis2() :
    i = randint(0, n-1)
    assert lev_dis(L[i][:1000],L[i][:1000]) == 0

"""Test Performance"""

#Test temporel
def test_lev_dis3() :
    i = randint(0, n-1)
    j = randint(0, n-1)
    assert timeit.timeit(lambda:"lev_dis(L[i][:1000], L[j][:1000])", number=10)/10 <= len(L[i])*len(L[j])/(10**9)
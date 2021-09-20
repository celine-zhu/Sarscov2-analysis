# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:46:12 2020

@author: HPCF1504A
"""
from math import sqrt
from var_leng_aa import var_leng_aa

#L est une liste de séquences, les séquences étant des listes de chaînes de caractère, chaque chaîne de caractère correspondant à un acide aminé
#aa est une chaîne de caractère correspondant à un acide aminé
def et_leng_aa(L):
    return sqrt(var_leng_aa(L))


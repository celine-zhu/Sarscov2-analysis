# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:48:21 2020

@author: HPCF1504A
"""
from var_leng import var_leng
from codons import codons

def var_leng_aa(L):
    return var_leng(codons(L))

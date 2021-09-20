# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:05:43 2020

@author: HPCF1504A
"""
from mediane import mediane
import timeit

def test_mediane1():
    assert mediane([['A'],['A','B','C'],['A','B']])==2

def test_mediane2():
    T=timeit.timeit(lambda:mediane([['A'],['A','B','C'],['A','B']]),number=1)
    assert T<=10
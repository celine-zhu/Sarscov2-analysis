# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:06:22 2020

@author: HPCF1504A
"""
from motfind import motfind
import timeit 
def test_motfind():
    assert motfind(['a','B','A','C','A','B','B','A','A','B','B','A'])==2
    
    
def test_motfind1():
    T=timeit.timeit(motfind(['a','B','A','C','A','B','B','A','A','B','B','A']))
    assert T<=10
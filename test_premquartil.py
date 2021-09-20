# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:02:44 2020

@author: HPCF1504A
"""
from premquartil import premquartil
def test_premquartil1():
    assert premquartil([['A'],['A','B','C'],['A','B']])==1
    
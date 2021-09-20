# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:10:12 2020

@author: HPCF1504A
"""
from et_leng_aa import et_leng_aa
import timeit

def test_et_leng_aa():
    assert et_leng_aa([['A'],['B'],['C'],['D'],['A','B']])==1
    
    
def test_et_leng_aa1():
    T=timeit.timeit(et_leng_aa([['A'],['B'],['C'],['D'],['A','B']]))
    assert T <=10
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:10:46 2020

@author: HPCF1504A
"""

from var_leng_aa import var_leng_aa
import timeit

def test_var_leng_aa():
    assert var_leng_aa([['A'],['B'],['C'],['D'],['A','B']])==0
    
    
def test_var_leng_aa1():
    s= len([['A'],['B'],['C'],['D'],['A','B']])
    assert timeit.timeit(lambda:"var_leng_aa([['A'],['B'],['C'],['D'],['A','B']]))", number=10)/10 < s*30000/(10**9)

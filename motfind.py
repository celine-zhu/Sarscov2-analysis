# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:45:04 2020

@author: HPCF1504A
"""

def motfind(L,motif):
    """trouve le motif dans la liste du genome"""
    sequence=''.join(L)#transforme la liste en string
    return sequence.count(motif)#trouve le nombre de motif dans ce string
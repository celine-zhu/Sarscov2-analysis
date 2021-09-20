# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:53:48 2020

@author: HPCF1504A
"""
def premquartil(L):
    """prend en argument une liste de string et renvoie 
    le premier quartile du nombre de lettres par sequences"""
    quart=[]
    n=len(L)

    for k in range(0,n):
        quart.append(len(L[k]))
    quart=sorted(quart) 
    N=int(len(quart)//4)
    if len(quart)%4==0:
        return quart[int(len(quart)//4)-1]
    else:
        return quart[N]
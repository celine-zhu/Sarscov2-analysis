# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:17:27 2020

@author: HPCF1504A
"""

def mediane(L):
    """prend en argument une liste de string et renvoie 
    la mediane de la longueur par sequences"""
    med=[]
    n=len(L)
    
    for k in range(0,n):
        med.append(len(L[k]))
    med=sorted(med)
    N=int((len(med)-1)/2)
    if len(med)%2==0:
        return (med[int((n+1)/2)]+med[int((n-1)/2)])/2
    else:
        return med[N]
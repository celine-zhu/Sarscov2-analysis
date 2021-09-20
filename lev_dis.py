# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:18:12 2020

@author: Cecla
"""
import numpy as np
import copy


def lev_dis(seq1, seq2):
    """fonction suivant l'algorithme de la distance de Leveshtein prenant en
    argument deux listes et rendant un entier(algorithme tire de wikipedia)"""
    m = len(seq1)
    n = len(seq2)
    v1 = np.zeros(n+1)
    v2 = np.zeros(n+1)

    for k in range(0,n):
        v1[k] = k

    for l in range (0,m):
        v2[0] = l+1

        for d in range(0,n):

            deletionCost = v1[d+1]+1
            insertionCost = v2[d]+1

            if seq1[l] == seq2[d]:
                substitutionCost = v1[d]
            else:
                substitutionCost = v1[d] + 1

            v2[d+1] = min(deletionCost,insertionCost,substitutionCost)

        T = copy.deepcopy(v1)
        v1 = copy.deepcopy(v2)
        v2 = copy.deepcopy(T)

    return v1[n]

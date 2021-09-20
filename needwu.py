# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:50:41 2020

@author: Cecla
"""
import numpy as np

#Pour acceder facilement aux éléments de la matrice de similarité
def ind(char) :
    if char == 'A' :
        return 0
    elif char == 'G' :
        return 1
    elif char == 'C' :
        return 2
    else :
        return 3


def matriF(A,B,S,d):
    """algorithme de la matrice prenant en arguments deux chaines de caracteres
    et en sortie une matrice F"""
    a=len(A)
    b=len(B)
    F=np.zeros((a,b))

    for i in range(0,a):
        F[i][0]=d*i

    for j in range(0,b):
        F[0][j]=d*j

    for i in range(1,a):

        for j in range(1,b):
            Choice1=F[i-1][j-1]+S[ind(A[i])][ind(B[j])]
            Choice2=F[i-1][j]+d
            Choice3=F[i][j-1]+d
            F[i][j]=max(Choice1,Choice2,Choice3)

    return F


def needwu(A,B,S,d):
    """application de l'algorithme needlewunch, prend en argument deux listes"""
    AlignementA=""
    AlignementB=""
    F=matriF(A,B,S,d)
    i=len(A)-1
    j=len(B)-1

    while i>0 and j>0:
        score=F[i][j]
        scorediag=F[i-1][j-1]
        scoreup=F[i][j-1]
        scoreleft=F[i-1][j]

        if score==(scorediag+S[ind(A[i])][ind(B[j])]):
            AlignementA=A[i]+AlignementA
            AlignementB=B[j]+AlignementB
            i=i-1
            j=j-1

        elif score==(scoreleft+d):
            AlignementA=A[i]+AlignementA
            AlignementB="-"+AlignementB
            i=i-1

        elif score==(scoreup+d):
            AlignementA="-"+AlignementA
            AlignementB=B[j]+AlignementB
            j=j-1

    while i>0:
        AlignementA=A[i]+AlignementA
        AlignementB="-"+AlignementB
        i=i-1

    while j>0:
        AlignementA="-"+AlignementA
        AlignementB=B[j]+AlignementB
        j=j-1

    return AlignementA, AlignementB




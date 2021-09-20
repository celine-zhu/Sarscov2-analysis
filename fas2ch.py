# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:03:36 2020

@author: HPCF1504A"""
from Bio import SeqIO
def fas2ch(seqfast):
    """extrait les séquences genetiques du fichier fasta 
    et les garde dans une liste L"""
    L=[]
    for seq_record in SeqIO.parse(seqfast, "fasta"):
        L.append(list(seq_record.seq.strip()))    
    return L     
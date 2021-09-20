import pytest
import timeit
from date import date
from fas2ch import fas2ch

#Teste ce qu'il se passe si l'annee n'existe pas
def test_date1() :
    assert date(2021,1) == []

#Teste ce qu'il se passe si le mois est trop petit
def test_date2() :
    assert date(2020,0) == []

#Teste ce qu'il se passe si le mois est trop grand
def test_date3() :
    assert date(2020,13) == []

#Verifie que les sequences retournees sont les bonnes, en supposant que la fonction fas2ch marche
def test_date4() :
    assert date(2020,1) == fas2ch("Sequences_2020_01.fasta")
    assert date(2020,2) == fas2ch("Sequences_2020_02.fasta")
    assert date(2020,3) == fas2ch("Sequences_2020_03.fasta")
    assert date(2020,4) == fas2ch("Sequences_2020_04.fasta")
    assert date(2020,5) == fas2ch("Sequences_2020_05.fasta")
    assert date(2020,6) == fas2ch("Sequences_2020_06.fasta")
    assert date(2020,7) == fas2ch("Sequences_2020_07.fasta")
    assert date(2020,8) == fas2ch("Sequences_2020_08.fasta")
    assert date(2020,9) == fas2ch("Sequences_2020_09.fasta")
    assert date(2020,10) == fas2ch("Sequences_2020_10.fasta")
    assert date(2020,11) == fas2ch("Sequences_2020_11.fasta")

#Test temporel
"""la complexité de date est en O((nombre de sequences dans le mois) * (longueur maximale d'une sequence))
On considère que les sequences ont une longueur d'environ 30 000 nucléotides, et que l'ordinateur exécute 10**9 opérations par secondes."""
def test_date5() :
    assert timeit.timeit(lambda:"date(2020,4)", number=10)/10 < 2*len(date(2020,4))*30000/(10**9)
from premquartil import premquartil
from timeit import timeit
from date_aa import date_aa
from premquartil_aa import premquartil_aa

def test_premquartil_aa():
    assert premquartil_aa(date_aa(2020,2)) == premquartil(date_aa(2020,2))
    assert premquartil_aa(date_aa(2020,4)) == premquartil(date_aa(2020,4))

def test_time_mediane_aa():
    L=date_aa(2020,1)
    time=timeit(lambda:premquartil_aa(L),number=1)
    M=[]
    for i in range (0,len(L)):
        M.append(len(L[i]))
    t=max(M)
    x=t*len(L)*30000/10**9
    assert time<=x
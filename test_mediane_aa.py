from mediane import mediane
from timeit import timeit
from date_aa import date_aa
from mediane_aa import mediane_aa

def test_mediane_aa():
    assert mediane_aa(date_aa(2020,2)) == mediane(date_aa(2020,2))
    assert mediane_aa(date_aa(2020,4)) == mediane(date_aa(2020,4))

def test_time_mediane_aa():
    L=date_aa(2020,1)
    time=timeit(lambda:mediane_aa(L),number=1)
    M=[]
    for i in range (0,len(L)):
        M.append(len(L[i]))
    t=max(M)
    x=t*len(L)*30000/10**9
    assert time<=x

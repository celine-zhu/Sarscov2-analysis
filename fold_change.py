def fold_change(f,L1,L2,*args):
    a=f(L1,*args)   #appliquer la fonction au premier ensemble de séquences
    b=f(L2,*args)   #appliquer la fonction au deuxieme ensemble de séquences

    if b==0:
        return 0

    return a/b

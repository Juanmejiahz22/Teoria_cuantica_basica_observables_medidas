import calcu_cplx as lib
import numpy as np
def proba_pos(v1,p1):
    norm = lib.normvect(v1)
    pos = lib.module_vector(v1[p1])**2
    respu = round(((pos/norm)**2)*100,2)
    return respu 

def proba_tran(v1,v2):
    lis1 = []
    for i in range(len(v2)):
        tem = [v2[i]]
        lis1 += [tem]
    v2 = lib.conjumat(lis1)
    lis2 = []
    for i in range(len(v2)):
        lis2 += v2[i]
    norm1 = lib.normvect(v1)
    norm2 = lib.normvect(lis2)
    norm = norm1 * norm2
    prob = [lib.val_ine(lis2,v1)]
    pun = lib.val_escal((1/norm,0),prob)[0]
    pun = (round(pun[0],2),round(pun[1],2))
    return pun
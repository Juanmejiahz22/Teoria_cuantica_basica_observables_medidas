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
    
def varianza(observable, K):
    Ket_aux = []
    for index in range(len(K)):
        aux = [K[index]]
        Ket_aux += [aux]
    Bra = lib.conjumat(Ket_aux)
    med = media(observable, K)
    id_med = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                id_med[i][j] = libreria.multicplx((-1, 0), med)
    id_med = lib.sumamatcplx(id_med, observable)
    cudrado = lib.mult_matrices(id_med, id_med)
    action = lib.accionmat(cudrado, Ket_aux)
    return lib.val_ine(action, Bra)
    
def mat_diagonal(m):
    m1 = [[(0, 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                m1[i][j] = (1, 0)
    return m1

def media(observable, K):
    K_aux = []
    for index in range(len(K)):
        aux = [K[index]]
        K_aux += [aux]
    if libreria.mat_hermitani(observable):
        vel = libreria.conjugar_matrix(K_aux)
        ac = libreria.accion_matrix(observable, K_aux)
        punto = libreria.val_ine(ac, vel)
        punto = (round(punto[0], 2), round(punto[1], 2))
        return punto
    else:
        return "No es un observable"
    
def valores_vectores(observable):
    valores, vectores = np.linalg.eig(observable)
    lista_valores = []
    lista_vectores = []
    for index in range(len(valores)):
        lista_valores += [(valores[index].real, valores[index].imag)]
    for index in range(len(vectores)):
        vector = []
        for index_2 in range(len(vectores[0])):
            vector += [(vectores[index][index_2].real, vectores[index][index_2].imag)]
        lista_vectores += [vector]
    return lista_valores, lista_vectores


def probabilidades_vectores(inicial, observable, posicion):
    vectores = valores_vectores(observable)
    return amplitud(inicial, vectores[posicion])

def dinamica(mat_u, v1, t):
    if libreria.verifi_mat_unitary(mat_u):
        for index in range(t):
            v1 = libreria.accion_matrix(mat_u, v1)
        return v1
    else:
        return "Matriz no valida"

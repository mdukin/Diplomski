import numpy as np
from ogr import ogr_nejednakosti, ogr_jednakosti
from hooke_jeeves import hooke_jeeves

def trans_u_prob_bez_ogr(X0,f, ogr_nejedn:ogr_nejednakosti, ogr_jedn:ogr_jednakosti, t = 1, epsilon = 10e-20):

    f_cilja = lambda X : f(X) + (1/t) * ogr_nejedn.mjesovito(X) + t * ogr_jedn.mjesovito(X)

    if not ogr_nejedn.zadovoljava(X0) :
        X = ogr_nejedn.vrati_tocku_koja_zad_ogr(X0)
        print("poc_tocka_koja_zad_ogr:", X)
    else:
        X = X0.copy()

    for _ in range(1000) :

        X_last = X.copy()
        X = hooke_jeeves(X,f_cilja)
        t *=10
        if np.linalg.norm(X-X_last) < epsilon:
            break
    return X
import numpy as np
from sympy import *


def Points_values(jacobian: Matrix, Array_Var: list, Values: list):
    temp = jacobian
    for i, j in zip(Array_Var, Values):
        temp = temp.subs(i, j)

    return np.array(temp, dtype=float)


def Next_Step(result: Matrix, Array_Var, X_0):

    # Hallar el paso con la solucion del Sel
    h = Points_values((result), Array_Var, X_0)

    # vector de paso
    h = h.flatten()

    return X_0+h


def Newton_Raphson(matrix: Matrix, Array_Var, Array_initial, epsilon):

    Array_initial = np.array(Array_initial)

    # Sel = Matrix([d_1, d_2, d_3, d_4, d_5, d_6,
    #  d_7, d_8, d_9, d_10, d_11, d_12])

    jacobian = matrix.jacobian(Array_Var)
    # Resultado de jacobino con el vector Sel
    result = jacobian.LUsolve(matrix)
    result = (result*-1)
    X_0 = np.array(Array_initial)
    X_1 = np.zeros(len(X_0))

    norm = np.linalg.norm
    i = 0
    while (norm(X_0-X_1) > epsilon):
        if (i > 0):
            X_0 = X_1
        X_1 = Next_Step(result=result,
                        Array_Var=Array_Var, X_0=X_0, )
        i += 1

    return X_1, i

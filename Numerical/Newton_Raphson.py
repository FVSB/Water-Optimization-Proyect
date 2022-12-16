import numpy as np
from sympy import *


def Points_values(jacobian: Matrix, Array_Var: list, Values: list):
    temp = jacobian
    for i, j in zip(Array_Var, Values):
        temp = temp.subs(i, j)

    return np.array(temp, dtype=float)


def Next_Step(jacobian, Array_Var, X_0, vect):

    # Evaluar la matriz Jacobiana en el punto X_0
    a = Points_values(
        jacobian, Array_Var, X_0)
    # Evaluar el SEL en x_0
    b = Points_values((vect*-1), Array_Var, X_0)
    # Proximo paso
    h = np.linalg.solve(a, b)
    # vector de paso
    h = h.flatten()

    X_1 = X_0+h

    return X_1


def Newton_Raphson(matrix: Matrix, Array_Var, Array_initial, epsilon):
    Sel = matrix
    Array_initial = np.array(Array_initial)

    # Sel = Matrix([d_1, d_2, d_3, d_4, d_5, d_6,
    #  d_7, d_8, d_9, d_10, d_11, d_12])

    jacobian = matrix.jacobian(Array_Var)

    X_0 = np.array(Array_initial)
    X_1 = np.zeros(len(X_0))

    norm = np.linalg.norm
    i = 0
    while (norm(X_0-X_1) > epsilon):
        if (i > 0):
            X_0 = X_1
        X_1 = Next_Step(jacobian=jacobian,
                        Array_Var=Array_Var, X_0=X_0, vect=Sel)
        i += 1

    return X_1, i

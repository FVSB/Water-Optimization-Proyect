from sympy import *
import numpy as np
#from Newton_Raphson import *
from Numerical.Newton_Raphson_LU import *

# α β   δ  h


def Solve_Numerical(a, b, d, h, Con_Concen_1, Con_Concen_2, Array_initial: list, epsilon=0.01):
    # Variables
    x = symbols('x')
    y = symbols('y')
    z_1 = symbols('z_1')
    z_2 = symbols('z_2')
    m_1 = symbols('m_1')
    m_2 = symbols('m_2')
    m_3 = symbols('m_3')
    m_4 = symbols('m_4')
    m_5 = symbols('m_5')
    m_6 = symbols('m_6')
    l_1 = symbols('λ_1')
    l_2 = symbols('λ_2')
    C_max_1 = Con_Concen_1
    C_max_2 = Con_Concen_2
    # Funciones
    d_1 = h*(-b+1/2*d)-m_1+m_3
    d_2 = h*(a+b)-m_2-m_3+(l_1*C_max_1)
    d_3 = -m_1*x
    d_4 = -m_2*z_2
    d_5 = m_2*(x-y-z_1)
    d_6 = C_max_1*(z_1+y)-(C_max_2*y)-m_1
    d_7 = h*(a+b)-m_4+m_6
    d_8 = h*(a+b)-m_5-m_6+l_2*C_max_2
    d_9 = -m_4*y
    d_10 = -m_5*z_2
    d_11 = m_6*(y-x-z_2)
    d_12 = C_max_2*(z_2+x)-(C_max_1*x)-m_2

    Array_Var = [x, y, z_1, z_2, l_1, l_2, m_1, m_2, m_3, m_4,
                 m_5, m_6]

    matrix = Matrix([[d_1], [d_2], [d_3], [d_4], [d_5], [d_6],
                    [d_7], [d_8], [d_9], [d_10], [d_11], [d_12]])

    return Newton_Raphson(matrix, Array_Var, Array_initial, epsilon)

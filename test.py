import pulp as lp

# cargar la librería PuLP

# Problema de programación lineal
prob = lp.LpProblem("test_de_optimizacion", lp.LpMinimize)

# Variables
# 0 <= x <= 4
x = lp.LpVariable("x", 0, 4)
# -1 <= y <= 1
y = lp.LpVariable("y", -1, 1)

# Objetivo
prob += x + 4*y, "obj"  # Restricciones
prob += x+y <= 5, "c1"
prob += x-y >= -2, "c2"


prob.solve()
print(" Impresión de los valores de las variables óptimas")
# Impresión de los valores de las variables óptimas
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("--------------------------------------------------------------------------------")
print("Valor óptimo de la función objetivo:", lp.value(prob.objective))
# Valor objetivo
print("objective=", lp.value(prob.objective))


def fff():
    '''x:is a float'''
    return 4


fff()

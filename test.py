import pulp as lp

# cargar la librería PuLP

# Problema de programación lineal
prob = lp.LpProblem("test_de_optimizacion_Empresa 1", lp.LpMinimize)
# Variables
# Empresa 1 Region
# 0 <= x <= 4
x = lp.LpVariable("Agua_Bombeada_por_la_Empresa_1_a_2", 0, 4)
# Concentracion Máxima de entrada Empresa 1
# 0<=xCin<=4
xC_in = lp.LpConstraint(4)
# Concentracion Maxima Salida Empresa 1
# 0<=xC_out<=4
xC_out = lp.LpConstraint(4)

# endRegion Empresa 1


# 1 <= y <= 10
y = lp.LpVariable("Cant_Agua_Bombeada_por_la_Empresa_2", 1, 10)

yC_in = lp.LpConstraint(4)
# Concentracion Maxima Salida Empresa 2
# 0<=xC_out<=4
yC_out = lp.LpConstraint(4)


# Suministro de agua del lider
# 1<=z<=10    siempre z>=0
z = lp.LpVariable("Suministro_de_agua_del_lider", 0, 10)

precio_Agua_Lider = lp.LpConstraint(25)

precio_Bombear_Agua_Entre_Empresas = lp.LpConstraint(
    40)

C_Out_Lider = lp.LpConstraint(20)

precio_Desechar_Agua = lp.LpConstraint(10)

Lider_Solver = z*precio_Agua_Lider

Desechos = (precio_Desechar_Agua*(z+y-x))
time = lp.LpConstraint(1)


# Objetivo
prob += time*(Lider_Solver+Desechos +
              ((1/2)*precio_Bombear_Agua_Entre_Empresas*(x+y))), "obj"
# Restricciones
prob += z >= 0, "c1"
prob += x >= 0, "c2"
prob += yC_out+C_Out_Lider >= xC_in, "c3"
prob += z+y >= x, "c4"

prob.solve()
print(" Impresión de los valores de las variables óptimas")
# Impresión de los valores de las variables óptimas
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("--------------------------------------------------------------------------------")
print("Valor óptimo de la función objetivo:", lp.value(prob.objective))
# Valor objetivo
print("objective=", lp.value(prob.objective))

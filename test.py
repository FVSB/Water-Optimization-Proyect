import pulp as pl
from Solver import Solve
from Auxiliar_Class import Process, Company
from Input import Read_Excel


def Start(Time_of: int):
    Company_list = Read_Excel()
    Solution = []
    for i in range(Time_of):
        sol = Solve(Company_list[0].Process_list[0],
                    Company_list[1].Process_list[0])
        c = sol.objective
        print()
        print(" Impresión de los valores de las variables óptimas")
    # Impresión de los valores de las variables óptimas
        for v in Solve.variables():
            print(v.name, "=", v.varValue)
            print(
                "--------------------------------------------------------------------------------")
            print("Valor óptimo de la función objetivo:",
                  pl.value(sol.objective))
            # Valor objetivo
            print("objective=", pl.value(sol.objective))

        Solution.append(
            Solve(Company_list[0].Process_list[0], Company_list[1].Process_list[0]))


def Input():
    # Importar datos de excel
    import pandas as pd
    a = pd.read_excel("DataBase.xlsx", index_col=0)
    b = a.to_dict()


Start(1)

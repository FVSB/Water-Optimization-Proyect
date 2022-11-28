import pulp as pl
from Solver import Solve
from Auxiliar_Class import Process, Company
from Input import Read_Excel
from Output import Output


def Start(Time_of: int):
    # Leer el archivo de excel
    Company_list = Read_Excel()

    # Por la cant de veces a realizar el proceso
    for i in range(Time_of):
        # Respuesta del solver
        sol = Solve(Company_list[0].Process_list[0],
                    Company_list[1].Process_list[0])
        # Coste optimo
        Total_Cost = pl.value(sol.objective)
        # Añadir valores de las varibles
        xs = sol.variables()
        # Cant de agua que debe proporcionar el lider
        Leader_water_supply = float(xs[0].varValue)
        # Agua que va del proceso 1 al 2
        Water_From_1_to_2 = float(xs[1].varValue)
        # Agua que va del proceso 2 al 1
        Water_From_2_to_1 = float(xs[2].varValue)
        # Serializar en el excel
        Output(str(Company_list[0].Process_list[0].Name), Total_Cost=Total_Cost,
               Leader_Supply=Leader_water_supply, Water_from_1_to_2=Water_From_1_to_2,
               Water_from_2_to_1=Water_From_2_to_1, filename="Output.xlsx")


def main():
    count = input("How many times do you want to run the program? ")
    Start(count)
    print("Done!")


# Iniciar programa
main()

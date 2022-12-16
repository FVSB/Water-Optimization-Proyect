import pulp as pl
import os
from Core.Solver import Solve
from Core.Auxiliar_Class import Process, Company
from Core.Input import Read_Excel, Read_Folder
from Core.Output import Output, Output_Numerical
from Numerical.Test import Solve_Numerical


def Numerical_Solution(Process_1: Process, Process_2: Process, Time_of: int, file):

    Water_From_2_to_1 = Process_2.Process_To_send[(
        Process_1.Company, Process_1.Name)][0]
    Water_From_1_to_2 = Process_1.Process_To_send[(
        Process_2.Company, Process_2.Name)][0]
    start = [Water_From_1_to_2, Water_From_2_to_1, Process_1.State_Max_Water_Supply,
             Process_2.State_Max_Water_Supply,
             Process_1.C_Max_Out, 0.1, 0.1, 0.1, 0.1, 0.1,
             0.1, 0.1]
    s, i = Solve_Numerical(a=Process_1.Sale_Price_State_Supply, b=Process_1.Price_discharge_water,
                           Con_Concen_1=Process_1.Con_Contamination, Con_Concen_2=Process_2.Con_Contamination, d=Process_1.Price_discharge_water, h=Time_of, Array_initial=start)
    Output_Numerical(str(Process_1.Name), s, file)


def Start(Time_of: int):
    # Leer el archivo de excel
    All_tupples = Read_Folder()
    for t in All_tupples:
        path = os.path.join("Data_Base", t)
        Company_list = Read_Excel(path)
        Output_name = "Output "+t
        # Solucion numerica
        Numerical_Solution(Company_list[0].Process_list[0],
                           Company_list[1].Process_list[0], Time_of, Output_name)
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
                   Water_from_2_to_1=Water_From_2_to_1, filename=Output_name)


def main():
    count = int(input("How many times do you want to run the program? "))
    Start(count)
    print("Done!")


# Iniciar programa
main()

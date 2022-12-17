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


def Solution(Process_to_analysis: Process, Process_to_buy_Water: Process):
    temp = {}
    Process_1 = Process_to_analysis.Name
    Process_2 = Process_to_buy_Water.Name

    for j in range(2):
        Process_1_ofert = Process_to_buy_Water.Process_To_send[(
            Process_to_analysis.Company, Process_to_analysis.Name)][0]
        sol = Solve(process_1=Process_to_analysis, process_2=Process_to_buy_Water
                    )
        # Coste optimo
        Total_Cost = pl.value(sol.objective)
        # Añadir valores de las varibles
        xs = sol.variables()
        # Cant de agua que debe proporcionar el lider
        Leader_water_supply = float(xs[0].varValue)
        # Agua que va del proceso 1 al 2
        Water_From_Hear_To_Other = Process_1_ofert
        # Agua que va del proceso 2 al 1
        Water_From_Other_To_Hear = float(xs[1].varValue)
        # Nombre del proceso  [Costo , Agua que debe proporcionar el lider, Agua que va del proceso al otro proceso, Agua que viene del otro proceso]
        temp[Process_to_analysis.Name] = [Total_Cost, Leader_water_supply,
                                          Water_From_Hear_To_Other, Water_From_Other_To_Hear]
        # Cambiar los valores de los procesos dado que se conoce el valor
        # que va del primer proceso al segundo
        Process_to_buy_Water.Process_To_send[(
            Process_to_analysis.Company, Process_to_analysis.Name)][0] = Water_From_Hear_To_Other

        # Swap los procesos
        be = Process_to_analysis
        af = Process_to_buy_Water
        Process_to_analysis = af
        Process_to_buy_Water = be

        # Arreglar el valor de venta real del Primer
        # proceso a analizar pq este asume que el 2do
        # le compra todo la oferta de agua
        if (j > 0):
            t = temp[Process_1][3]
            val = temp[Process_2][3]
            temp[Process_1][2] = val

    return temp, Process_to_analysis, Process_to_buy_Water


def Start(Time_of: int):
    # Leer el archivo de excel
    All_tupples = Read_Folder()
    for t in All_tupples:
        path = os.path.join("Data_Base", t)
        Company_list = Read_Excel(path)
        Output_name = "Output "+t
        Process_to_analysis = Company_list[0].Process_list[0]
        Process_to_buy_Water = Company_list[1].Process_list[0]
        # Solucion numerica
        Numerical_Solution(Process_1=Process_to_analysis,
                           Process_2=Process_to_buy_Water, Time_of=Time_of, file=Output_name)
        # Por la cant de veces a realizar el proceso
        dicc = {int: dict}
        x = 0
        for i in range(Time_of):
            # Respuesta del solver
            temp, Process_to_analysis, Process_to_buy_Water = Solution(
                Process_to_analysis, Process_to_buy_Water)

            # Agregar a diccionario
            dicc[i] = temp
            x += 1
            # Serializar en el excel
        Output(filename=Output_name, dicc=dicc, Process_1_Name=Process_to_analysis.Name,
               Process_2_Name=Process_to_buy_Water.Name, x=x)


def main():
    count = int(input("How many times do you want to run the program? "))
    Start(count)
    print("Done!")


# Iniciar programa
main()

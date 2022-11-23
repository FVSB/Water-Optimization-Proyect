from Clases import Intermediary, Process, Company
#import solver
import pulp as pl

# Propuesta de agua de sumunistrar del proceso from al proceso B


def Sum_Process_From_A_to_B(dic_From_A_to_B: dict[Process, list[Process]], Dic_LpVariable: dict[(Process, Process), pl.LpVariable], ProcessFrom: Process):
    list_process_To = dic_From_A_to_B[Process]
    A: pl.LpVariable = None
    for destino in list_process_To:
        A += Dic_LpVariable[(ProcessFrom, destino)]
    return A


def Make_a_process(inter: Intermediary, process_Temp: Process):

    Leader_Water_price = inter.Price_Leader_Water
    Price_Sell_Water = inter.Price_Sell_Water
    obj = None

    # Cant de agua desde otros procesos hasta el proceso_Temp
    sum_Process_B_to_process_Temp = Intermediary.Get_The_Sum_Of_The_From_A_To_B(
        company_Temp)
    # Cant de agua del procesos Temp ha otros
    sum_Process_From_process_Temp_to_B = Sum_Process_From_A_to_B(
        inter.DicFrom_To, inter.Dic_pl_Variables, process_Temp)

    # Leader
    Leader_Supply = pl.LpVariable(
        "Leader_Water_Supply", lowBound=0, upBound=process_Temp.Cant_Water_Leader, cat="Continuous")
    Fresh_Water = Leader_Water_price*Leader_Supply

    # Discharge Water
    Discharge_Price = process_Temp.Price_Discharged_Water * \
        (sum_Process_B_to_process_Temp+Leader_Supply -
         sum_Process_From_process_Temp_to_B)

    # Transport Water
    Transport_Price = (
        Price_Sell_Water/2)*(sum_Process_B_to_process_Temp+sum_Process_From_process_Temp_to_B)

    # obj
    obj += Fresh_Water+Discharge_Price+Transport_Price
    restriccion_1 = Leader_Supply >= 0 and Leader_Supply <= process_Temp.Cant_Water, "c1"
    restriccion_2 = sum_Process_B_to_process_Temp + \
        Leader_Supply >= process_Temp.Cant_Water, "c7"

    return [obj, restriccion_1, restriccion_2]


def Solver(Intermediario: Intermediary):
    inter = Intermediario
    prob = pl.LpProblem("Water", pl.LpMinimize)
    for Company in Intermediario.List_of_Company:
        for process in Company.List_of_Process:
            temp = Make_a_process(inter, process)
        prob += temp[0], process.Company+" "+process.Name
        prob += temp[1], process.Company+" "+process.Name
        prob += temp[2], process.Company+" "+process.Name

    prob.solve()

    print(" Impresión de los valores de las variables óptimas")
    # Impresión de los valores de las variables óptimas
    for v in prob.variables():
        print(v.name, "=", v.varValue)
        print("--------------------------------------------------------------------------------")
        print("Valor óptimo de la función objetivo:", pl.value(prob.objective))
        # Valor objetivo
        print("objective=", pl.value(prob.objective))

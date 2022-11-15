import pulp as pl
from Clases import Process
import Input as ip


def Solver(process_1: Process, process_2: Process, Water_from_1_to_2: float, Water_From_2_1, Price_transport_water: float, Leader_Water_price: float, Water_Leader_supply: float, Fresh_Water_Contamination: float = 0.0):
    prob = pl.LpProblem("Water", pl.LpMinimize)

    # X: cant de agua que se envia de 1 a 2
    x = pl.LpVariable("Water_From_1_To_2", lowBound=0,
                      upBound=Water_from_1_to_2, cat="Continuous")

    # Y: cant de agua que se envia de 2 a 1
    y = pl.LpVariable("Water_From_2_To_1", lowBound=0,
                      upBound=Water_From_2_1, cat="Continuous")

    # LEADER
    Leader_Supply = pl.LpVariable(
        "Leader_Water_Supply", lowBound=0, upBound=Water_Leader_supply, cat="Continuous")
    Fresh_Water = Leader_Water_price*Leader_Supply

    # Discharge Water
    Discharge_Price = process_1.Price_Discharged_Water*(y+Leader_Supply-x)

    # Transport Water
    Transport_Price = Price_transport_water/2*(x+y)

    # Objective Function
    obj = Fresh_Water+Discharge_Price+Transport_Price
    prob += obj, "obj"
    prob += obj >= 0.00000001, "c1"
    prob += Leader_Supply >= 0 and Leader_Supply <= process_1.Cant_Water, "c4"
    prob += process_2.C_Max_Out+Fresh_Water_Contamination <= process_1.C_Max_In, "c5"
   # prob += process_1.C_Max_Out+Fresh_Water_Contamination <= process_2.C_Max_In, "c6"
    prob += y+Leader_Supply >= process_1.Cant_Water, "c7"

   # return
    prob.solve()
    prob.to_json("prob.json")
    print(" Impresión de los valores de las variables óptimas")
    # Impresión de los valores de las variables óptimas
    for v in prob.variables():
        print(v.name, "=", v.varValue)
        print("--------------------------------------------------------------------------------")
        print("Valor óptimo de la función objetivo:", pl.value(prob.objective))
        # Valor objetivo
        print("objective=", pl.value(prob.objective))


def Start():
    listProcess = ip.CreateProcess(2)
    process_1 = listProcess[0]
    process_2 = listProcess[1]

    Water_from_1_to_2 = float(input("Water from 1 to 2: "))
    Water_from_2_to1 = float(input("Water from 2 to 1: "))
    Leader_Water_price = float(input("Leader Water Price: "))
    Leader_Water_Supply = float(input("Leader Water Supply: "))
    Price_transport_water = float(input("Price transport water: "))
    prob = Solver(process_1, process_2, Water_from_1_to_2,
                  Water_from_2_to1, Price_transport_water, Leader_Water_price, Leader_Water_Supply)


Start()

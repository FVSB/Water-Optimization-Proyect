import pulp as pl
from Auxiliar_Class import Process


def Solve(process_1: Process, process_2: Process):
    # Declaracion de variables

    Water_From_1_to_2 = process_1.Process_To_send[(
        process_2.Company, process_2.Name)][0]
    Water_From_2_to_1 = process_2.Process_To_send[(
        process_1.Company, process_1.Name)][0]

    Water_Leader_supply = process_1.State_Max_Water_Supply
    Leader_Water_price = process_1.Sale_Price_State_Supply

    Price_Transport_water = process_1.Process_To_send[(
        process_2.Company, process_2.Name)][1]
    # Invocar una nuevo problema del solver de pulp (minimizar)
    prob = pl.LpProblem("Water", pl.LpMinimize)

    # X: cant de agua que se envia de 1 a 2
    x = pl.LpVariable(str("Water From "+str(process_1.Company)+str(process_1.Name)+" To "+str(process_2.Company)+str(process_2.Name)), lowBound=0,
                      upBound=Water_From_1_to_2, cat="Continuous")

    # Y: cant de agua que se envia de 2 a 1
    y = pl.LpVariable(str("Water From "+str(process_2.Company)+str(process_2.Name)+" To "+str(process_1.Company)+str(process_1.Name)), lowBound=0,
                      upBound=Water_From_2_to_1, cat="Continuous")

    # Lider
    Leader_Supply = pl.LpVariable(
        "Leader_Water_Supply", lowBound=0, upBound=Water_Leader_supply, cat="Continuous")
    Fresh_Water = Leader_Water_price*Leader_Supply

    # Agua a descargar
    Discharge_Price = process_1.Price_discharge_water*(y+Leader_Supply-x)

    # Transportar agua
    Transport_Price = Price_Transport_water/2*(x+y)

    # Objective Function
    obj = float(process_1.time_of_test) * \
        (Fresh_Water+Discharge_Price+Transport_Price)
    # Agragar la funcion objetivo al problema
    prob += obj, "obj"
    # Agragar consicion al problema
    prob += Leader_Supply >= 0 and Leader_Supply <= float(
        process_1.Cant_Water), "c1"
    prob += float(process_2.C_Max_Out) <= float(process_1.C_Max_In), "c2"
    prob += y+Leader_Supply >= float(process_1.Cant_Water), "c3"

    prob.solve()
# return
    return prob

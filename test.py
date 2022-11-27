import pulp as pl
import Solver as sl

def CreateProcess(count):
    array: list[Process] = []
    for i in range(count):
        name = input("Nombre del Proceso: ")

        C_Max_in = float(input("Contaminacion Maxima de Entrada: "))

        C_Max_out = float(input("Contaminacion Maxima de Salida: "))

        Cant_Water = float(input("Cantidad de Agua para el proceso: "))

        array.append(Process(name, C_Max_in, C_Max_out,
                             Cant_Water))

    return array


def Start():
    listProcess = CreateProcess(2)
    process_1 = listProcess[0]
    process_2 = listProcess[1]

    Water_from_1_to_2 = float(input("Water from 1 to 2: "))
    Water_from_2_to1 = float(input("Water from 2 to 1: "))
    Leader_Water_price = float(input("Leader Water Price: "))
    Leader_Water_Supply = float(input("Leader Water Supply: "))
    Price_transport_water = float(input("Price transport water: "))
    prob = sl.Solver.Solve(process_1, process_2, Water_from_1_to_2,
                           Water_from_2_to1, Price_transport_water, Leader_Water_price, Leader_Water_Supply)
    prob.to_json("prob.json")
    print(" Impresión de los valores de las variables óptimas")

    # Impresión de los valores de las variables óptimas
    for v in prob.variables():
        print(v.name, "=", v.varValue)
        print("--------------------------------------------------------------------------------")
        print("Valor óptimo de la función objetivo:", pl.value(prob.objective))
        # Valor objetivo
        print("objective=", pl.value(prob.objective))


Start()

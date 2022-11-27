
from Clases import Intermediary, Process, Company
import Solver as sl

arrayProcess: list[Process] = []


def CreateCompany(count):
    array: list[Company] = []
    for i in range(count):
        x = (Company(input("Nombre de la Empresa: "),
                     CreateProcess(int(input("Cuantos Procesos Desea Crear?")
                                       )
                                   )
                     )
             )
        array.append(x)
        arrayProcess.append(x)

    return array

# Creacion de Procesos


def CreateProcess(count):
    array: list[Process] = []
    for i in range(count):
        name = input("Nombre del Proceso: ")

        C_Max_in = float(input("Contaminacion Maxima de Entrada: "))

        C_Max_out = float(input("Contaminacion Maxima de Salida: "))

        Cant_Water = float(input("Cantidad de Agua para el proceso: "))

        Cant_Water_Discharged = float(input(
            "Cantidad de Agua que se descarga: "))

        Price_Discharged_Water = float(input("Precio de Agua Descargada: "))

        Price_Sell_Water = float(input("Precio de Venta del Agua: "))

        array.append(Process(name, C_Max_in, C_Max_out,
                             Cant_Water, Cant_Water_Discharged, Price_Discharged_Water, Price_Sell_Water))

    return array

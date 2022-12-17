
import pandas as pd
import os
import numpy as np
# Serializar en el excel

"""
def Output(Process_name: str, Total_Cost, Leader_Supply, Water_from_1_to_2, Water_from_2_to_1, filename):
    # Crear el dataframe
    df = pd.DataFrame(
        # Proceso                   Costo Optimo              Agua que debe proporcionar el lider               Agua que va del proceso 1 al 2               Agua que va del proceso 2 al 1
        {"Process": [Process_name], "Total Cost": [Total_Cost],
         "Leader Supply": [Leader_Supply], "Water From 1 to 2": [Water_from_1_to_2], "Water From 2 to 1": [Water_from_2_to_1]})
   # Guardar en la carpeta de salida
    path = os.path.join("Output", filename)
    # Guardar el dataframe en un excel
    df.to_excel(path, sheet_name=Process_name, index=False)
"""

# [Total_Cost, Leader_water_supply,
#  Water_From_Hear_To_Other, Water_From_Other_To_Hear]


def Output(dicc: dict, Process_1_Name: str, Process_2_Name: str, x: int, filename):
    iteraciones = []

    Cant_Agua_1_hacia_2 = []
    Cant_Agua_2_hacia_1 = []
    Precio_1 = []
    Precio_2 = []
    Cant_agua_estado_1 = []
    Cant_agua_estado_2 = []
    for i in range(x):
        temp = dicc[i]
        iteraciones.append(i)

        array_1 = temp[Process_1_Name]
        Precio_1.append(array_1[0])
        Cant_agua_estado_1.append(array_1[1])
        Cant_Agua_1_hacia_2.append(array_1[2])

        array_2 = temp[Process_2_Name]
        Precio_2.append(array_2[0])
        Cant_agua_estado_2.append(array_2[1])
        Cant_Agua_2_hacia_1.append(array_2[2])

    df = pd.DataFrame({"Iteracion ": iteraciones, str("Precio "+Process_1_Name): Precio_1, str("Precio "+Process_2_Name): Precio_2,
                       str("Cant_Agua_del_estado "+Process_1_Name): Cant_agua_estado_1, str("Cant_Agua_del_estado "+Process_2_Name): Cant_agua_estado_2,
                       str("De "+Process_1_Name+" Hacia "+Process_2_Name): Cant_Agua_1_hacia_2,
                       str("De "+Process_2_Name+" Hacia "+Process_1_Name): Cant_Agua_2_hacia_1})
    path = os.path.join("Output", str(filename))
    df.to_excel(path, sheet_name="solu", index=False)


def Output_Numerical(Process_name, Array, filename):

    df = pd.DataFrame(
        {"Process": [Process_name], "Water_from_1_to_2": [Array[0]], "Water_from_2_to_1": [Array[1]],
         "Leader_Water_Supply_1": [Array[2]], "Leader_Water_Supply_2": [
            Array[3]],
         "λ_1": [Array[4]], "λ_2": [Array[5]],
         "μ_1": [Array[6]], "μ_2": [Array[7]],
         "μ_3": [Array[8]], "μ_4": [Array[9]],
         "μ_5": [Array[10]], "μ_6": [Array[11]]}
    )
    path = os.path.join("Output", str("Numerical"+filename))
    df.to_excel(path, sheet_name=Process_name, index=False)

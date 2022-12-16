
import pandas as pd
import os
import numpy as np
# Serializar en el excel


def Output(Process_name: str, Total_Cost, Leader_Supply, Water_from_1_to_2, Water_from_2_to_1, filename):
    # Crear el dataframe
    df = pd.DataFrame(
        # Proceso                   Costo Optimo              Agua que debe proporcionar el lider               Agua que va del proceso 1 al 2               Agua que va del proceso 2 al 1
        {"Process": [Process_name], "Total Cost": [Total_Cost], "Leader Supply": [Leader_Supply], "Water From 1 to 2": [Water_from_1_to_2], "Water From 2 to 1": [Water_from_2_to_1]})
   # Guardar en la carpeta de salida
    path = os.path.join("Output", filename)
    # Guardar el dataframe en un excel
    df.to_excel(path, sheet_name=Process_name, index=False)


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

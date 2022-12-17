import pandas as pd
import os.path
from os import listdir
from Core.Auxiliar_Class import Process, Company

# Buscar el nombre de todas las hojas del excel


def nameAllSheets(filename):
    if not os.path.isfile(filename):
        return None
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    return sheets

# Crear la clase Company


def Create_Company(Dicc: pd.DataFrame, Name: str) -> Company:

    process_Name = Dicc['Process'][0]
    C_Max_In = Dicc['C_Max_In'][0]
    C_Max_out = Dicc['C_Max_Out'][0]
    Process_Water_Consumption = Dicc['Process Water Consumption'][0]
    State_Water_Supply = Dicc['State´s Water Supply'][0]
    Sale_State_Water_Price = Dicc["State´s water price"][0]
    Time_of_test = Dicc['Time of test'][0]
    Company_to_send = Dicc['Company to send'][0]
    Process_to_send = Dicc['Process to send'][0]
    Max_water_Supply_To_Other = Dicc['Max water Supply'][0]
    Price_supply_water = Dicc['Price supply water'][0]
    Price_discharge_water = Dicc["Discharge water price"][0]
    Con_Contamination=Dicc["Con_Contamination"][0]
    # Crear un proceso
    process1 = Process(Name=process_Name, Company=Name, C_Max_In=C_Max_In, C_Max_Out=C_Max_out, Cant_Water=Process_Water_Consumption,
                       State_Max_Water_Supply=State_Water_Supply, Sale_Price_State_Supply=Sale_State_Water_Price,
                       Time_of_Test=Time_of_test, Price_discharge_water=Price_discharge_water,
                       Process_To_send={(Company_to_send, Process_to_send): [Max_water_Supply_To_Other, Price_supply_water]},Con_Contamination=Con_Contamination)
    # Crear la compañia
    return Company(Process_list=[process1], Name=Name)


def Read_Folder(path: str = "Data_Base") -> list:
    return listdir(path)


def Read_Excel(Path: str)->list[Company]:
    # Leer el archivo de excel y guardar en un diccionario
    a = pd.read_excel(Path, sheet_name=None, header=None, skiprows=1, names=["Process", "C_Max_In", "C_Max_Out",
                                                                             "Process Water Consumption", "State´s Water Supply",
                                                                             "State´s water price", "Discharge water price", "Time of test", "Company to send",
                                                                             "Process to send", "Max water Supply", "Price supply water","Con_Contamination"])

    Company_list = []

    for i in nameAllSheets(Path):
        x = a.pop(i)
        Company_list.append(Create_Company(x.to_dict(), i))

    return Company_list

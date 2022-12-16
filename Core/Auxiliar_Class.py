
class Process:  # Please with the name of the process write the company that is going to do it
    def __init__(self, Name: str, Company: str, C_Max_In: float, C_Max_Out: float, Cant_Water: float, State_Max_Water_Supply: float, Sale_Price_State_Supply: float, Time_of_Test: float, Process_To_send: dict, Price_discharge_water: float,Con_Contamination:float):
        self.Name = Name
        self.Company = Company
        self.C_Max_In = C_Max_In
        self.C_Max_Out = C_Max_Out
        self.Cant_Water = Cant_Water
        self.State_Max_Water_Supply = State_Max_Water_Supply
        self.Sale_Price_State_Supply = Sale_Price_State_Supply
        self.time_of_test = Time_of_Test
        self.Process_To_send = Process_To_send
        self.Price_discharge_water = Price_discharge_water
        self.Con_Contamination = Con_Contamination
    def __str__(self):
        return "Name: "+self.Name+" C_Max_In: "+self.C_Max_In+" C_Max_Out: "+self


class Company:
    def __init__(self, Name: str, Process_list: list[Process]):
        self.Name = Name
        self.Process_list = Process_list

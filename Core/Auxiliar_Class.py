
class Process:  # Please with the name of the process write the company that is going to do it
    def __init__(self, Name: str, Company: str, C_Max_In: float, C_Max_Out: float, Cant_Water: float, State_Max_Water_Supply: float, Sale_Price_State_Supply: float, Time_of_Test: float, Process_To_send: dict, Price_discharge_water: float, Con_Contamination: float):
        self.Name = Name
        self.Company = Company
        self.C_Max_In = float(C_Max_In)
        self.C_Max_Out = float(C_Max_Out)
        self.Cant_Water = float(Cant_Water)
        self.State_Max_Water_Supply = float(State_Max_Water_Supply)
        self.Sale_Price_State_Supply = float(Sale_Price_State_Supply)
        self.time_of_test = float(Time_of_Test)
        self.Process_To_send = Process_To_send
        self.Price_discharge_water = float(Price_discharge_water)
        self.Con_Contamination = float(Con_Contamination)

    def __str__(self):
        return "Name: "+self.Name+" C_Max_In: "+self.C_Max_In+" C_Max_Out: "+self

    def water_Supply_Other(self, other):
        if (self.C_Max_Out > other.C_Max_In):
            return 0
        return self.Process_To_send[(other.Company, other.Name)][0]

    def Price_Supply_Water(self, other):
        if (self.C_Max_Out > other.C_Max_In):
            return 0
        return self.Process_To_send[(other.Company, other.Name)][1]

    def How_Much_buy(self, other):
        ofer = other.water_Supply_Other(self)
        cost = other.Price_Supply_Water(self)
        if (self.Sale_Price_State_Supply < cost):
            return 0
        if (ofer > self.Cant_Water):
            return self.Cant_Water
        else:
            return ofer

    def stateSupply(self):
        if (self.State_Max_Water_Supply > self.Cant_Water):
            return self.Cant_Water
        else:
            return self.State_Max_Water_Supply


class Company:
    def __init__(self, Name: str, Process_list: list[Process]):
        self.Name = Name
        self.Process_list = Process_list

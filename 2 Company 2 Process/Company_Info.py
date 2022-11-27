
class Process:  # Please with the name of the process write the company that is going to do it
    def __init__(self, Name: str, C_Max_In: float, C_Max_Out: float, Cant_Water: float):
        self.Name = Name
        self.C_Max_In = C_Max_In
        self.C_Max_Out = C_Max_Out
        self.Cant_Water = Cant_Water

    def __str__(self):
        return "Name: "+self.Name+" C_Max_In: "+self.C_Max_In+" C_Max_Out: "+self

    def AddCompany(self, Company):
        self.Company = Company

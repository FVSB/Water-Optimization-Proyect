import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Process:  # Please with the name of the process write the company that is going to do it
    def __init__(self, Name: str, C_Max_In: float, C_Max_Out: float, Cant_Water: float, Cant_Discharged_Water: float, Price_Discharged_Water: float, Price_Sell_Water: float, Cant_Water_Leader: float = -1):
        self.Name = Name
        self.C_Max_In = C_Max_In
        self.C_Max_Out = C_Max_Out
        self.Price_Sell_Water = Price_Sell_Water
        self.Cant_Discharge_Water = Cant_Discharged_Water
        self.Price_Discharged_Water = Price_Discharged_Water
        self.Cant_Water = Cant_Water
        self.Cant_Water_Leader = Cant_Water_Leader
        if (self.Cant_Water_Leader < 0):
            self.Cant_Water_Leader = self.Cant_Water

    def __str__(self):
        return "Name: "+self.Name+" C_Max_In: "+self.C_Max_In+" C_Max_Out: "+self

    def AddCompany(self, Company):
        self.Company = Company


class Company:
    def __init__(self, Name, List_of_Process: list[Process]):
        self.Name = Name
        self.List_of_Process = List_of_Process

    def AddProcess(self, Process):
        self.List_of_Process.append(Process)
        Process.AddCompany(self)


class Intermediary:
    def __init__(self, List_of_Company: list[Company], Price_Leader_Water: float):
        self.List_of_Company = List_of_Company
        self.Dic = self.Filter({})
        self.Price_Leader_Water = Price_Leader_Water
        # Dado un proceso A Proceso de partida,B Proceso de llegada, Cantidad de agua que se va a usar
        self.DicTemp: dict[(Process, Process): float] = {}
        # Este dicc anota desde el proceso A que puede ofrecer agua al proceso B
        self.DicFrom_TO = dict[Process, list[Process]] = {}

    # This function is to filter the process that are going to be used

    def Filter(self, dicc: dict[Process, list[Process]]):
        # This function will be changed because it is not the best way to do it but it is the easiest
        # Select a company
        for i in self.List_of_Company:
            # In this company select a process
            for j in i.List_of_Process:
                # Compare With the other different process
                for a in self.List_of_Company:
                    for b in a.List_of_Process:
                        # If the process is different
                        if (i.name != a.name or j.name != b.name):
                            # if the C_Max_Out of the process is less than the C_Max_In of the other process
                            if (j.C_Max_In >= b.C_Max_Out):
                                dicc[j].append(b)
                                self.DicFrom_To[b].append(j)
        return dicc

    # This function is to choose the process that are going to be used
    def Choice_The_Possibles(self):

        for i in self.Dic.keys():
            for j in self.Dic[i]:
                print(i.Name, "  From ", i.Company,
                      " The Contamination it's ", i.C_Max_In)
                print("can be used with")
                print(j.Name, "  From ", j.Company, " The Contamination it's ", j.C_Max_Out,
                      " The Price of sell is ", j.Price_Sell_Water)
                a = input("Do you want to use this process? (Y/N)")
                clear()
                if (a == "N"):
                    self.Dic[i].remove(j)
                    self.DicFrom_To[j].remove(i)
                else:
                    count = input("How much water do you want to use?")
                    # From_To
                    self.DicTemp[(i, j)] = count
        return self.DicTemp

    def Get_The_Possibles_Process(self, Process: Process):
        return self.Dic[Process]
        # This function is to choose the process that are going to be used

    def Get_The_Possibles_From(self, Process: Process):
        return self.DicFrom_To[Process]
      # Esta funcion indica cuales procesos pueden ir del proceso A en analisis a otro B

    def Get_The_Posibles_Count(self, ProcessFrom: Process, ProcessTo: Process):
        return float(self.DicTemp[(ProcessFrom, ProcessTo)])

# cargar la librería PuLP
import pulp as lp
# Cargar Biblioteca de Clases
import Clases as cl


class Solver:

    def __init__(self, Intermediary: cl.Intermediary):
        self.Intermediary = Intermediary
        self.WaterLeaderPrice = Intermediary.Price_Leader_Water

    def Solver_To(self, Company_name: str,
                  Process: cl.Process):
        process = Process

        # Problema de programación lineal
        prob = lp.LpProblem(Company_name, lp.LpMinimize)
        # Constantes Fijas del problema :Precio del agua del lider
        Leader_Water_Price = lp.LpConstraint(self.WaterLeaderPrice)
        Count_Leader_Water = lp.LpVariable(
            "Leader Water Supply", 0, process.Cant_Water_Leader)
        # Precio a Pagar al lider
        Buy_Leader_Price = Leader_Water_Price*Count_Leader_Water

        # Precio de Desechar Agua

        Water_Discard_Price = lp.LpConstraint(process.Price_Discard_Water)

        listTemp = self.Intermediary.Get_The_Possibles_Process(process)

        SumWaterFromProcess_From_B_To_A = None

        for i in range(len(listTemp)):
            # Agua de otros procesos para el proceso P

            processTemp = listTemp[i]
            Water_From_B_To_A = lp.LpVariable(
                "Water_From_B_To_A", 0, cl.Intermediary.Get_The_Posibles_Count(processTemp, process))
            SumWaterFromProcess += Water_From_B_To_A

        # Cantidad de agua que envio de un proceso a otro

        SumWaterFromProcess_From_A_To_B = None
        listFrom_A_To_B = self.Intermediary.Get_The_Possibles_From(process)
        for i in range(len(listFrom_A_To_B)):
            processTemp = listFrom_A_To_B[i]
            Water_From_A_To_B = lp.LpVariable(
                "Water_From_A_To_B", 0, cl.Intermediary.Get_The_Posibles_Count(process, processTemp))
            SumWaterFromProcess_From_A_To_B += Water_From_A_To_B

        # X es β(Agua del lider+Agua de otros procesos para el proceso P-Agua que envio de un proceso a otro)
        x = Water_Discard_Price * \
            (Count_Leader_Water+SumWaterFromProcess_From_B_To_A -
             SumWaterFromProcess_From_A_To_B)
        # Y es el precio de transporte de agua de un proceso a otro
        y = process.Price_Transport_Water/2 * \
            (SumWaterFromProcess_From_A_To_B+SumWaterFromProcess_From_B_To_A)

        # Función Objetivo
        prob += Buy_Leader_Price+x+y, "obj"
        # Restricciones
        prob += Count_Leader_Water >= 0, "c1"
        prob += SumWaterFromProcess_From_B_To_A >= 0, "c2"
        prob += SumWaterFromProcess_From_A_To_B >= 0, "c3"
        prob += Count_Leader_Water + \
            SumWaterFromProcess_From_B_To_A >= SumWaterFromProcess_From_A_To_B, "c4"
        prob += Count_Leader_Water+SumWaterFromProcess_From_B_To_A >= process.Cant_Water, "c5"

        prob.solve()

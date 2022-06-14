from numpy import dtype
from datetime import date, datetime
import os
import pandas as pd

# from api.eurodatahos_vs_shrepoint import EuroShare
from api.sap_vs_sharepoint import SapShare


Week = '01'
today = date.today().strftime("%d%m%y")
path_data_input = "InputData/processes.xlsx"
# path_data_sharepoint = "E:/AppTotalEnergies/SRC-Python-comparaison/InputData/sharepoint1.xlsx"
# path_Out = f"OutputData/KPI-SIS-AFRIQUE-S{Week}-{today}.xlsx"
path_Out = f"OutputData/SAP_vs_Sharepoint_1-{today}.xlsx"

df_hos = pd.read_excel(r"C:\Users\J1049122\Desktop\Station Data\SAP\ALL Data SAP brute 13.06.2022.xlsx", sheet_name="AFR")
df_sharepoint = pd.read_excel(r"C:\Users\J1049122\Desktop\Station Data\SAP\ALL Data SAP brute 13.06.2022.xlsx", sheet_name="StationData")

start = datetime.now()
m = SapShare(df_hos, df_sharepoint, path_Out)
m.reduce()

# os.system('cls' if os.name == 'nt' else 'clear')
# print(type(df_hos))
print()
print("--------------------")
print("Terminer avec succès")
print("--------------------")
print()

end = datetime.now()
tm = end - start
print("temps d'exécution :", tm)
print()













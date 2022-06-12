from numpy import dtype
from api.eurodatahos_vs_shrepoint import EuroShare
from datetime import date, datetime
import os
import pandas as pd


Week = '01'
today = date.today().strftime("%d%m%y")
path_data_input = "InputData/processes.xlsx"
# path_data_sharepoint = "E:/AppTotalEnergies/SRC-Python-comparaison/InputData/sharepoint1.xlsx"
path_Out = f"OutputData/KPI-SIS-AFRIQUE-S{Week}-{today}.xlsx"

df_hos = pd.read_excel(path_data_input, sheet_name="DataApp_S04-22")
df_sharepoint = pd.read_excel(path_data_input, sheet_name="sharepoint")

start = datetime.now()
# m = EuroShare(df_hos, df_sharepoint, path_Out)
# m.reduce()

# os.system('cls' if os.name == 'nt' else 'clear')
print(type(df_hos))
print("--------------------")
print("Terminer avec succès")
print("--------------------")
print()

end = datetime.now()
tm = end - start
print("temps d'exécution :", tm)
print()













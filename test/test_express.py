from numpy import dtype
from datetime import date, datetime
import os
import pandas as pd

from api.eurodatahos_vs_shrepoint import EuroShare
from api.sap_vs_stationData import SapShare


Week = '01'
today = date.today().strftime("%d%m%y")
path_data_input = r"C:\Users\J1049122\Desktop\Station Data\SAP\SAP_STATIONDATA.xlsx"
# path_data_sharepoint = "E:/AppTotalEnergies/SRC-Python-comparaison/InputData/sharepoint1.xlsx"
# path_Out = f"OutputData/KPI-SIS-AFRIQUE-S{Week}-{today}.xlsx"
path_Out = f"OUT/SAP_vs_Sharepoint-test-{today}.xlsx"

df_hos = pd.read_excel(r"Input/SAP.xlsx", keep_default_na=False)
df_sharepoint = pd.read_excel(r"Input/StationData.xlsx", keep_default_na=False)

# df_hos=df_hos.drop_duplicates(subset = "SAPCODE", keep = 'first')

# df_hos = SapShare(df_hos, 'df_sharepoint', path_Out).preprocess(df_hos.drop('COUNTRYCODE', axis=1))
# # df_hos['COUNTRYCODE'] = df_hos['SAPCODE'].str.slice(0, 2)
# df_hos.to_excel('df_sap.xlsx', index=False)

start = datetime.now()
m = SapShare(df_hos, df_sharepoint, path_Out)
m.reduce()

# os.system('cls' if os.name == 'nt' else 'clear')
# print(type(df_hos))

# xls = pd.ExcelFile(path_data_input)
# print(xls)
# print()
# print(xls.sheet_names)

print()
print("--------------------")
print("Terminer avec succès")
print("--------------------")
print()

end = datetime.now()
tm = end - start
print("temps d'exécution :", tm)
print()













import pandas as pd
import numpy as np
import os

from openpyxl import load_workbook
from tqdm import tqdm


class SapShare:
    def __init__(self, df_sap, df_stationData, path_Out):
        self.df_sap = df_sap
        self.df_stationData = df_stationData
        self.path_Out = path_Out

    def comparer(self, df_X, df_Y, col, texte = True):
        self.diff_X = np.setdiff1d(df_X[col] ,df_Y[col])
        self.ecart_X = df_X.loc[df_X[col].isin(self.diff_X)]
        
        if texte:
            print("Données SAP versus données stationData :")
            print(f"il y'a {len(self.diff_X)} code SAP de différence")
            print()
        
        self.diff_Y = np.setdiff1d(df_Y[col], df_X[col])
        self.ecart_Y = df_Y.loc[df_Y[col].isin(self.diff_Y)]
        
        if texte:
            print("Données stationData versus données SAP :")
            print(f"il y'a {len(self.diff_Y)} code SAP de différence")

        self.commun = df_X.loc[~df_X[col].isin(self.diff_X)]

        return self.ecart_X, self.ecart_Y, self.commun
    
    def LoadData(self, typ, path, sheet=""):
        if typ == '.csv':
            self.df = pd.read_csv(path, dtype=str, keep_default_na=False)
        elif typ in ['.xls', 'xlsx']:
            if sheet is None or sheet == "":
                self.df = pd.read_excel(path, keep_default_na=False)
            else:
                self.df= pd.read_excel(path, sheet_name=sheet, dtype=str, keep_default_na=False)
        else:
            pass
        return self.df

    def preprocess(self, df):
        df['SAPCode'] = df['SAPCode'].astype(str)
        df['SAPCode'] = df['SAPCode'].str.strip()
        df['SAPCode'] = df['SAPCode'].str.upper()

        df['IsActiveSite'] = df['IsActiveSite'].astype(str)
        df['IsActiveSite'] = df['IsActiveSite'].str.strip()
        df['IsActiveSite'] = df['IsActiveSite'].str.upper()

        df['BusinessModel'] = df['BusinessModel'].astype(str)
        df['BusinessModel'] = df['BusinessModel'].str.strip()
        df['BusinessModel'] = df['BusinessModel'].str.upper()

        df = df.drop_duplicates(subset = "SAPCode", keep = 'first')
        # df['COUNTRYCODE'] = df['SAPCode'].str.slice(0, 2)
    
        return df
    
    def Preprocess_Sap(self, df):
        df['COUNTRYCODE'] = df['SAPCode'].str.slice(0, 2)
        df['CountryCode'] = df['COUNTRYCODE']
        df = df[[
            'SAPCode', 'SAPName', 'Zone', 'Affiliate', 'BusinessModel', 'IsActiveSite', 'CountryCode', 'Town', 'Address', 'DealerCode', 'DealerName', 'SiteTel', 'COUNTRYCODE'
        ]]
        df = self.preprocess(df)
        # df['IsActiveSite'] = df['IsActiveSite'].apply(lambda x: "VRAI" if x == "TRUE" else "FAUX")
        return df
    
    def Preprocess_stationData(self, df):
        df['COUNTRYCODE'] = df['SAPCode'].str.slice(0, 2)
        df = self.preprocess(df)
        return df
    
    def Merge_Data(self, df_sap, df_sh):
        cols = list(df_sh.columns)
        df_sh = df_sh.drop_duplicates(subset = 'COUNTRYCODE', keep = 'first')[['SubZone', 'COUNTRYCODE']]

        df_sap = df_sap.merge(df_sh, how='left', on='COUNTRYCODE')

        # supprimer les nan dans la colonne Affiliate méthode 1
        # dd = df_sap.drop_duplicates(subset = "COUNTRYCODE", keep = 'first')
        # dd.index = range(len(dd))
        # for i in range(dd.shape[0]):
        #     if pd.isna(dd['Affiliate'][i]):
        #         df_sap = df_sap[df_sap['COUNTRYCODE'] != dd['COUNTRYCODE'][i]]

        # supprimer les nan dans la colonne Affiliate méthode 2
        df_sap = df_sap.dropna(subset=['Affiliate'])
        
        # ajouter les colonnes manquantes de df_stationData
        for col in list(self.df_stationData.drop(list(df_sap.columns), axis=1).columns):
            df_sap[col] = ""

        # reorganiser les colonnes de df_sap comme df_stationData
        df_sap = df_sap.reindex(columns = cols)
        return df_sap

    def export_excel(self, path, df, SheetName):
        self.writer_list = pd.ExcelWriter(path, engine='openpyxl')
        df.to_excel(self.writer_list, sheet_name=SheetName, index=False)
        self.writer_list.save()
        self.writer_list.close()

    def export_excel_add_new_sheet(self, path, df, SheetName):
        self.book = load_workbook(path)
        self.writer_list = pd.ExcelWriter(path, engine='openpyxl')
        self.writer_list.book = self.book
        df.to_excel(self.writer_list, sheet_name=SheetName, index=False)
        self.writer_list.save()
        self.writer_list.close()

    def Update_EcartSAP_vs_sh(self, df_sap_commun_avec_sh, df_stationData):

        if df_sap_commun_avec_sh.shape[0] > 0:
            for j in tqdm(range(df_sap_commun_avec_sh.shape[0])):
                for k in range(df_stationData.shape[0]):
                    if df_sap_commun_avec_sh['SAPCode'].iloc[j] == df_stationData['SAPCode'].iloc[k] and df_sap_commun_avec_sh['BusinessModel'].iloc[j].strip().lower() != df_stationData['BusinessModel'].iloc[k].strip().lower():
                        df_stationData['BusinessModel'].iloc[k] = df_sap_commun_avec_sh['BusinessModel'].iloc[j]
                        df_stationData['BusinessModel_source'].iloc[k] = df_sap_commun_avec_sh['BusinessModel_source'].iloc[j]

                    if df_sap_commun_avec_sh['SAPCode'].iloc[j] == df_stationData['SAPCode'].iloc[k] and df_sap_commun_avec_sh['IsActiveSite'].iloc[j].strip().lower() != df_stationData['IsActiveSite'].iloc[k].strip().lower():
                        df_stationData['IsActiveSite'].iloc[k] = df_sap_commun_avec_sh['IsActiveSite'].iloc[j]
                        df_stationData['IsActiveSite_source'].iloc[k] = df_sap_commun_avec_sh['IsActiveSite_source'].iloc[j]
    
    def reduce(self):

        # charger les données EuroDataHOS et stationData
        # self.df_sap = self.LoadData('excel', self.path_data_HOS)
        # self.df_stationData = self.LoadData('excel', self.path_data_stationData)
        # df_sap_exp = self.preprocess(self.df_sap.drop('COUNTRYCODE', axis=1))
        # self.df_sap = self.df_sap[self.df_sap['COUNTRYCODE'] == "NA"]
        # self.df_stationData = self.df_stationData[self.df_stationData['Affiliate'] == "Namibia"]
        
        self.export_excel(path=self.path_Out, df=self.df_sap, SheetName='SAP All Zone')
        self.export_excel_add_new_sheet(path=self.path_Out, df=self.df_stationData, SheetName='stationData')

        # Prétraiter les données EuroDataHOS et stationData
        self.df_sap = self.Preprocess_Sap(self.df_sap)
        self.df_stationData = self.Preprocess_stationData(self.df_stationData)

        self.df_sap = self.Merge_Data(df_sap=self.df_sap, df_sh=self.df_stationData)

        # add column
        self.df_sap['BusinessModel_source'] = "SAP"
        self.df_stationData['BusinessModel_source'] = "STATION DATA"

        self.df_sap['IsActiveSite_source'] = "SAP"
        self.df_stationData['IsActiveSite_source'] = "STATION DATA"

        self.df_sap['Data_Source'] = "Ecart SAP"
        self.df_stationData['Data_Source'] = "STATION DATA"
        
        # comparaison sur le SAPCode
        self.ecart_sap, self.ecart_sh, self.df_sap_commun_avec_sh = self.comparer(
            df_X=self.df_sap, df_Y=self.df_stationData, col='SAPCode', texte=False
        )

        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("-"*23)
        print("Traitement en cours...")
        print("-"*23)
        print()
        
        # for pays in tqdm(self.df_sap_commun_avec_sh['Affiliate'].unique()):
        #     print()
        #     print("-"*35)
        #     print('Affiliates : ' + pays)
        #     print()

            # self.df_1 = self.df_sap_commun_avec_sh[self.df_sap_commun_avec_sh['Affiliate'] == pays]
            # self.df_2 = self.df_stationData[self.df_stationData['Affiliate'] == pays]
            # self.df_3 = self.ecart_sap[self.ecart_sap['Affiliate'] == pays]

        self.Update_EcartSAP_vs_sh(self.df_sap_commun_avec_sh, self.df_stationData)
        self.df_final = self.df_stationData.append(self.ecart_sap, ignore_index=True)
        self.export_excel_add_new_sheet(path=self.path_Out, df=self.df_final, SheetName="Comparaison")
        self.export_excel_add_new_sheet(path=self.path_Out, df=self.ecart_sh, SheetName="ecart stationData")
        # self.export_excel_add_new_sheet(path=self.path_Out, df=self.df_sap, SheetName="sap")
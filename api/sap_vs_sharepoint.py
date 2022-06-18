import pandas as pd
import numpy as np
import os

from openpyxl import load_workbook
from tqdm import tqdm


class SapShare:
    def __init__(self, df_sap, df_sharepoint, path_Out):
        self.df_sap = df_sap
        self.df_sharepoint = df_sharepoint
        self.path_Out = path_Out

    def comparer(self, df_X, df_Y, col, texte = True):
        self.diff_X = np.setdiff1d(df_X[col] ,df_Y[col])
        self.ecart_X = df_X.loc[df_X[col].isin(self.diff_X)]
        
        if texte:
            print("Données SAP versus données Sharepoint :")
            print(f"il y'a {len(self.diff_X)} code SAP de différence")
            print()
        
        self.diff_Y = np.setdiff1d(df_Y[col], df_X[col])
        self.ecart_Y = df_Y.loc[df_Y[col].isin(self.diff_Y)]
        
        if texte:
            print("Données Sharepoint versus données SAP :")
            print(f"il y'a {len(self.diff_Y)} code SAP de différence")

        self.commun = df_X.loc[~df_X[col].isin(self.diff_X)]

        return self.ecart_X, self.ecart_Y, self.commun
    
    def LoadData(self, typ, path, sheet=""):
        if typ == '.csv':
            self.df = pd.read_csv(path)
        elif typ in ['.xls', 'xlsx']:
            if sheet is None or sheet == "":
                self.df = pd.read_excel(path)
            else:
                self.df= pd.read_excel(path, sheet_name=sheet)
        else:
            pass
        return self.df


    def preprocess(self, df):
        df['SAPCODE'] = df['SAPCODE'].astype(str)
        df['SAPCODE'] = df['SAPCODE'].str.strip()
        df = df.drop_duplicates(subset = "SAPCODE", keep = 'first')
        df['BusinessModel'] = df['BusinessModel'].astype(str)
        df['BusinessModel'] = df['BusinessModel'].str.strip()
        df['COUNTRYCODE'] = df['SAPCODE'].str.slice(0, 2)

        return df
    
    def Preprocess_Sap(self, df):
        df = df[['SAPCODE', 'BusinessModel', 'IsActiveSite']]
        df = self.preprocess(df)
        return df
    
    def Preprocess_Sharepoint(self, df):
        df = self.preprocess(df)
        return df
    
    def Merge_Data(self, df_sap, df_sh):
        cols = list(df_sh.columns)
        df_sh = df_sh.drop_duplicates(subset = 'COUNTRYCODE', keep = 'first')[['Zone', 'SubZone', 'Affiliate', 'COUNTRYCODE']]
        df_sap = df_sap.merge(df_sh, how='left', on='COUNTRYCODE')

        # supprimer les nan dans la colonne Affiliate méthode 1
        # dd = df_sap.drop_duplicates(subset = "COUNTRYCODE", keep = 'first')
        # dd.index = range(len(dd))
        # for i in range(dd.shape[0]):
        #     if pd.isna(dd['Affiliate'][i]):
        #         df_sap = df_sap[df_sap['COUNTRYCODE'] != dd['COUNTRYCODE'][i]]

        # supprimer les nan dans la colonne Affiliate méthode 2
        df_sap = df_sap.dropna(subset=['Affiliate'])
        
        # ajouter les colonnes manquantes de df_sharepoint
        for col in list(self.df_sharepoint.drop(list(df_sap.columns), axis=1).columns):
            df_sap[col] = ""

        # reorganiser les colonnes de df_sap comme df_sharepoint
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

    def Update_EcartSAP_vs_sh(self, df_sap_commun_avec_sh, df_sharepoint):

        if df_sap_commun_avec_sh.shape[0] > 0:
            for j in tqdm(range(df_sap_commun_avec_sh.shape[0])):
                for k in range(df_sharepoint.shape[0]):
                    if df_sap_commun_avec_sh['SAPCODE'].iloc[j] == df_sharepoint['SAPCODE'].iloc[k] and df_sharepoint['BusinessModel'].iloc[k].lower() not in ['shop', 'stand', 'alone', 'standalone']:
                        df_sharepoint['BusinessModel'].iloc[k] = df_sap_commun_avec_sh['BusinessModel'].iloc[j]
                        df_sharepoint['BusinessModel_source'].iloc[k] = df_sap_commun_avec_sh['BusinessModel_source'].iloc[j]
    
    def reduce(self):

        # charger les données EuroDataHOS et sharepoint
        # self.df_sap = self.LoadData('excel', self.path_data_HOS)
        # self.df_sharepoint = self.LoadData('excel', self.path_data_sharepoint)
        df_sap_exp = self.preprocess(self.df_sap.drop('COUNTRYCODE', axis=1))
        
        self.export_excel(path=self.path_Out, df=df_sap_exp, SheetName='SAP sans doublons')
        self.export_excel_add_new_sheet(path=self.path_Out, df=self.df_sharepoint, SheetName='StationData Brute')

        # Prétraiter les données EuroDataHOS et sharepoint
        self.df_sap = self.Preprocess_Sap(self.df_sap)
        self.df_sharepoint = self.Preprocess_Sharepoint(self.df_sharepoint)

        self.df_sap = self.Merge_Data(df_sap=self.df_sap, df_sh=self.df_sharepoint)

        # add column
        self.df_sap['BusinessModel_source'] = "SAP"
        self.df_sharepoint['BusinessModel_source'] = "STATION DATA"
        self.df_sap['Data_Source'] = "Ecart SAP"
        self.df_sharepoint['Data_Source'] = "STATION DATA"
        
        # comparaison sur le SAPCODE
        self.ecart_sap, self.ecart_sh, self.df_sap_commun_avec_sh = self.comparer(
            df_X=self.df_sap, df_Y=self.df_sharepoint, col='SAPCODE', texte=False
        )

        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("-"*23)
        print("Traitement en cours...")
        print("-"*23)
        print()
        
        for pays in tqdm(self.df_sap_commun_avec_sh['Affiliate'].unique()):
            print()
            print("-"*35)
            print('Affiliates : ' + pays)
            print()

            self.df_1 = self.df_sap_commun_avec_sh[self.df_sap_commun_avec_sh['Affiliate'] == pays]
            self.df_2 = self.df_sharepoint[self.df_sharepoint['Affiliate'] == pays]
            self.df_3 = self.ecart_sap[self.ecart_sap['Affiliate'] == pays]

            self.Update_EcartSAP_vs_sh(self.df_1, self.df_2)

            self.df_final = self.df_2.append(self.df_3, ignore_index=True)

            self.export_excel_add_new_sheet(path=self.path_Out, df=self.df_final, SheetName=pays)
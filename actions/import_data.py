import tkinter as tk

from datetime import datetime
from tkinter import filedialog

from api.eurodatahos_vs_shrepoint import EuroShare


class Actions:
    def __init__(self) -> None:
        pass

    @staticmethod
    def ImportData(sheet=None, fileExtension=".xlsx"):
        """
        Cette grosse fonction permet d'abord d'ouvrir l'explorateur et parcourir le schéma du fichier, enssuite d'importer les données
        """
        filetype = ("xlsx files", f"*{fileExtension}") if fileExtension == ".xlsx" else ("CSV Files", "*.csv")
        path_filename = filedialog.askopenfilename(
            initialdir="E:\Total\Station Data\Master data\Data source",
            title="Select A File",
            filetype=(filetype, ("All Files", "*.*")),
        )

        if path_filename:
            """Si le fichier sélectionné est valide, cela chargera le fichier"""
            try:
                df = EuroShare(None, None, None).LoadData(typ=path_filename.split(".")[-1], path=path_filename)
                return path_filename, df
            except ValueError or AttributeError:
                tk.messagebox.showerror("Information", "Le fichier que vous avez choisi n'est pas valide")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"Fichier non trouvé {path_filename}")
                return None
        else:
            pass
    
    def ask_export_directory(self, type_output):
        if type_output == 'EuroShare':
            return filedialog.askdirectory() + f'/KPI-SIS-AFRIQUE-{datetime.today().strftime("%d-%m-%Y_%H%M%S")}.xlsx'
        return filedialog.askdirectory() + f'/Comparaison-SAP-vs-STATIONDATA_{datetime.today().strftime("%d-%m-%Y_%H%M%S")}.xlsx'
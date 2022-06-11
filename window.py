import tkinter as tk
import pandas as pd

from tkinter import PhotoImage
from datetime import date

from components.home import Home
from actions.import_data import ImportData
# from actions.import_data import Actions


class MainWindow():

    def __init__(self):
        # initialisation et configuration de fênetre principale
        self.root = tk.Tk()
        self.root.title("Data App Desktop")
        self.root.iconbitmap("static/img/TotalEnergies.ico")
        self.root.config(background="#BCBCBC")
        width, height = 550, 300
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = (height+10) + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        
        # charger les images et rédimenssionner
        self.excelIcon = PhotoImage(file="static/img/excel.png")
        self.excelIcon = self.excelIcon.subsample(10, 10)
        self.csvIcon = PhotoImage(file="static/img/csv.png")
        self.csvIcon = self.csvIcon.subsample(10, 10)
        self.viewIcon = PhotoImage(file="static/img/view.png")
        self.viewIcon = self.viewIcon.subsample(50, 50)
        
        # State
        # self.subject = ""
        # self.typefile = None
        # self.id = 0
        self.PathImport1 = ""
        self.PathImport2 = ""
        self.df1 = pd.DataFrame()
        self.df2 = pd.DataFrame()
        # self.PathExportFinal = ""
        # self.today = date.today().strftime("%d%m%y")
        # self.PathExport = ""

        self.home = Home(
            root = self.root, 
            excelIcon = self.excelIcon, 
            viewIcon = self.viewIcon,
            # PathImport11 = self.PathImport1,
            # df1 = self.df1,
            # import_data_1 = self.import_data_1,
            # PathImport2 = self.PathImport2,
            # df2 = self.df2,
            # import_data_2 = self.import_data_2,
        ).display()

    def start(self):
        self.root.mainloop()

    # def import_data_1(self):
    #     self.PathImport1, self.df1 = ImportData(self)
    #     print(self.PathImport1)
    #     print(self.df1.head(3))

    # def import_data_2(self):
    #     self.PathImport2, self.df2 = ImportData()
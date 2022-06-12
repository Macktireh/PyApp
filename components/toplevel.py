from cmath import e
from random import setstate
import tkinter as tk
import pandas

from tkinter import messagebox
from dataclasses import dataclass
from components import container_widget, container_button, table
from api.eurodatahos_vs_shrepoint import EuroShare
from actions.import_data import Actions

@dataclass
class Toplevel_Window():
    root: tk.Tk
    title: str
    source: str
    excelIcon: tk.PhotoImage
    viewIcon: tk.PhotoImage
    PathImport1: str = ""
    PathImport2: str = ""
    df1: pandas.core.frame.DataFrame = pandas.DataFrame()
    df2: pandas.core.frame.DataFrame = pandas.DataFrame()
        
    def display(self):
        self.TopWindow = tk.Toplevel(self.root)
        self.TopWindow.grab_set()
        self.TopWindow.title("Data App Desktop")
        self.TopWindow.iconbitmap("static/img/TotalEnergies.ico")
        self.TopWindow.geometry("700x500+30+40")
        self.TopWindow.resizable(width=False, height=False)
        
        self.header = tk.Frame(self.TopWindow, bd=4, bg="#FAEBD7", height=5)
        self.header.pack(side="top", fill="x")
        
        self.top_title = tk.Label(
            self.header,
            text=self.title,
            font=("Helvetica", 15),
            bg="#FAEBD7",)
        self.top_title.pack(side="bottom", fill="x")
        
        widget_1 = container_widget.Widget(
            root = self.TopWindow,
            title = self.source,
            excelIcon = self.excelIcon,
            viewIcon = self.viewIcon,
            x=0.02,
            y=0.08,
            import_data_from_excel=self.import_data_1,
            view_data=self.showTable_1
        )
        widget_1.display(
            self.PathImport1 if self.PathImport1 != "" else "test"
        )
        
        widget_2 = container_widget.Widget(
            root = self.TopWindow,
            title = 'Sharepoint',
            excelIcon = self.excelIcon,
            viewIcon = self.viewIcon,
            x=0.02,
            y=0.45,
            import_data_from_excel=self.import_data_2,
            view_data=self.showTable_2
        )
        widget_2.display(
            self.PathImport2 if self.PathImport2 != "" else "test"
        )
        
        container_btn = container_button.Widget(
            root=self.TopWindow,
            run_compare_files=self.run_compare_files
        )
        container_btn.display()
    
    def import_data_1(self):
        try:
            self.PathImport1, self.df1 = Actions.ImportData(self)
            return self.PathImport1, self.df1
        except AttributeError:
            messagebox.showerror("Information", "Le fichier que vous avez choisi n'est pas valide")

    def import_data_2(self):
        try:
            self.PathImport2, self.df2 = Actions.ImportData(self)
            return self.PathImport2, self.df2
        except AttributeError:
            messagebox.showerror("Information", "Le fichier que vous avez choisi n'est pas valide")

    def showTable_1(self):
        table.ShowData(root=self.TopWindow).display(self.PathImport1, self.df1)

    def showTable_2(self):
        table.ShowData(root=self.TopWindow).display(self.PathImport2, self.df2)
    
    def run_compare_files(self, path):
        EuroShare(self.df1, self.df2, path).reduce()
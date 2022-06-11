from random import setstate
import tkinter as tk
import pandas

from dataclasses import dataclass
from components import container_widget, container_button, table
from actions.import_data import ImportData

@dataclass
class Toplevel_Window():
    root: tk.Tk
    title: str
    source: str
    excelIcon: tk.PhotoImage
    viewIcon: tk.PhotoImage
    PathImport1: str = "s"
    PathImport2: str = ""
    df1: pandas.core.frame.DataFrame = pandas.DataFrame()
    df2: pandas.core.frame.DataFrame = pandas.DataFrame()
    # import_data_1: object
    # import_data_2: object
        
    def display(self):
        self.TopWindow = tk.Toplevel(self.root)
        self.TopWindow.grab_set()
        self.TopWindow.title("Data App Desktop")
        self.TopWindow.iconbitmap("static/img/TotalEnergies.ico")
        self.TopWindow.geometry("700x500+15+15")
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
            setState= self.state1,
            import_data_from_excel=self.import_data_1,
            view_data=table.ShowData(root=self.TopWindow, df=self.df1, path=self.PathImport1).display
        )
        widget_1.display()

        VarLabelPath = tk.StringVar()
        VarLabelPath.set(self.PathImport1)
        LabelPath = tk.Label(self.TopWindow, textvariable=VarLabelPath, bg="#C60030")
        LabelPath.pack(side="bottom", fill="x")
        
        widget_2 = container_widget.Widget(
            root = self.TopWindow,
            title = 'Sharepoint',
            excelIcon = self.excelIcon,
            viewIcon = self.viewIcon,
            x=0.02,
            y=0.45,
            setState=self.state2,
            import_data_from_excel=self.import_data_2,
            view_data=table.ShowData(root=self.TopWindow, df=self.df2, path=self.PathImport2).display
        )
        widget_2.display()
        
        container_btn = container_button.Widget(
            self.TopWindow,
            browse_button=self.import_data_1
        )
        container_btn.display()
    
    def import_data_1(self):
        self.PathImport1, self.df1 = ImportData(self)

    def import_data_2(self):
        self.PathImport2, self.df2 = ImportData()

    def state1(self):
        print(self.PathImport1)
        print(self.df1.head())
        return self.PathImport1, self.df1
        # return {'path': self.PathImport1, "df": self.df1}

    def state2(self):
        print(self.PathImport2)
        print(self.df2.head())
        return self.PathImport2, self.df2
        # return {'path': self.PathImport2, "df": self.df2}

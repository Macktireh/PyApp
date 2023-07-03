import tkinter as tk
import pandas

from dataclasses import dataclass
from tkinter import PhotoImage


@dataclass
class Widget:
    root: tk.Tk
    title: str
    excelIcon: tk.PhotoImage
    viewIcon: tk.PhotoImage
    x: float
    y: float
    import_data_from_excel: object
    view_data: object
    path: str = ""
    df: pandas.core.frame.DataFrame = pandas.DataFrame()

    def display(self):
        Frame = tk.LabelFrame(
            self.root, 
            text=self.title, 
            font=("Helvetica 10 bold"), 
            fg="#004C8C", labelanchor='n'
        )
        Frame.place(relx=self.x, rely=self.y, relheight=0.35, relwidth=0.96)
            
        self.VarLabelPath = tk.StringVar()
        self.VarLabelPath.set('Aucun fichier Excel importer')
        self.LabelPath = tk.Label(Frame, textvariable=self.VarLabelPath)
        self.LabelPath.pack(fill="x")

        excelBtn = tk.Button(
            Frame,
            image=self.excelIcon,
            text="Import data from Excel",
            compound="top",
            height=70,
            width=160,
            bd=1,
            bg="#DCDCDC",
            command=self.run_action,
            pady=2
        ).place(relx=0.23, rely=0.21)

        self.csvIcon = PhotoImage(file="static/img/csv.png")
        self.csvIcon = self.csvIcon.subsample(10, 10)
        csvBtn = tk.Button(
            Frame,
            image=self.csvIcon,
            text="Import data from CSV",
            compound="top",
            height=70,
            width=160,
            bd=1,
            bg="#DCDCDC",
            command=lambda: self.run_action(".csv"),
            pady=2
        ).place(relx=0.53, rely=0.21)

        ViewDataBtn = tk.Button(
            Frame,
            image=self.viewIcon,
            text=f"   Voir le données {self.title}",
            compound="left",
            height=20,
            width=190,
            bd=1,
            bg="#DCDCDC",
            command=self.view_data,
        ).place(relx=0.35, rely=0.8)

    def run_action(self, fileExtension=".xlsx"):
        try:
            self.path, self.df = self.import_data_from_excel(fileExtension=fileExtension)
            self.VarLabelPath.set(f'{self.path}')
        except:
            pass
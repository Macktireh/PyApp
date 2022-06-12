import tkinter as tk
import pandas

from tkinter import filedialog
from dataclasses import dataclass


from components.toplevel import Toplevel_Window


@dataclass
class Home():
    root: tk.Tk
    excelIcon: tk.PhotoImage
    viewIcon: tk.PhotoImage

    def display(self):

        self.Btn_SAP_vs_Sharepoint = tk.Button(
            self.root,
            text="SAP vs Sharepoint",
            background="#FAEBD7",
            activebackground="#0256CD",
            foreground="black",
            activeforeground="white",
            borderwidth=5,
            relief="raised",
            font=("Helvetica", 10),
            command=self.Window_SAP_vs_Sharepoint
        )
        self.Btn_SAP_vs_Sharepoint.place(relx=0.09, rely=0.2, relheight=0.15, relwidth=0.4)

        self.Btn_EuroDataHOS_vs_Sharepoint = tk.Button(
            self.root,
            text="EuroDataHOS vs Sharepoint",
            background="#FAEBD7",
            activebackground="#0256CD",
            foreground="black",
            activeforeground="white",
            borderwidth=5,
            relief="raised",
            font=("Helvetica", 10),
            command=self.Window_EuroDataHos_vs_Sharepoint
        )
        self.Btn_EuroDataHOS_vs_Sharepoint.place(relx=0.51, rely=0.2, relheight=0.15, relwidth=0.4)

        self.BtnExit = tk.Button(
            self.root,
            text="Quiter",
            background="#C60030",
            activebackground="#C60030",
            foreground="black",
            activeforeground="white",
            borderwidth=5,
            relief="raised",
            font=("Helvetica", 11),
            command=self.root.quit
        )
        self.BtnExit.place(relx=0.35, rely=0.6, relheight=0.15, relwidth=0.3)

    def Window_SAP_vs_Sharepoint(self):
        Toplevel_Window(
            root = self.root,
            title = "SAP versus Sharepoint",
            source = "SAP",
            excelIcon = self.excelIcon,
            viewIcon = self.viewIcon,
        ).display()
        
    def Window_EuroDataHos_vs_Sharepoint(self):
        Toplevel_Window(
            root = self.root,
            title = "EuroDataHos versus Sharepoint",
            source = "EuroDataHOS",
            excelIcon = self.excelIcon,
            viewIcon = self.viewIcon,
        ).display()


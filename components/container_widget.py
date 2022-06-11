import tkinter as tk
import pandas

from dataclasses import dataclass


@dataclass
class Widget():
    root: tk.Tk
    title: str
    excelIcon: tk.PhotoImage
    viewIcon: tk.PhotoImage
    x: float
    y: float
    import_data_from_excel: object
    view_data: object
    setState: object
    path: str = ""
    df: pandas.core.frame.DataFrame = pandas.DataFrame()

    def display(self):
            
        Frame = tk.LabelFrame(
            self.root, 
            text=self.title, 
            font=("Helvetica 10 bold"), 
            fg="#004C8C", labelanchor='n')
        Frame.place(relx=self.x, rely=self.y, relheight=0.35, relwidth=0.96)

            
        VarLabelPath = tk.StringVar()
        VarLabelPath.set(self.path)
        LabelPath = tk.Label(Frame, textvariable=VarLabelPath, bg="#FAEBD7")
        LabelPath.pack(fill="x")
        
        # Button import avec icon
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

        listbox = tk.Listbox(Frame)
        listbox.place(relx=0.65, rely=0.17, relheight=0.8, relwidth=0.3)
        
        treescrolly = tk.Scrollbar(listbox, orient="vertical", command=listbox.yview)
        treescrollx = tk.Scrollbar(listbox, orient="horizontal", command=listbox.xview)
        listbox.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

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

    def run_action(self):
        self.import_data_from_excel()
        self.path, self.df = self.setState()
        print(self.path, self.df)

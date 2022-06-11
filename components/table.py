import tkinter as tk

import pandas
from tkinter import ttk
from dataclasses import dataclass


@dataclass
class ShowData():
    root: tk.Tk
    # setState: str
    df: pandas.core.frame.DataFrame = pandas.DataFrame()
    path: str = ""

    def display(self):
        self.show_data = tk.Toplevel(self.root)
        self.show_data.title("Previous Data")
        self.show_data.iconbitmap("static/img/TotalEnergies.ico")
        self.show_data.geometry("800x450+15+15")
        self.show_data.resizable(width=False, height=False)
        
        # Add Some Style
        style = ttk.Style()

        # Pick A Theme
        style.theme_use("clam")

        # Configure the Treeview Colors
        style.configure(
            "Treeview.Heading",
            background="lightblue",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
        )

        # Change Selected Color
        style.map("Treeview", background=[("selected", "#347083")])

        def clear_data():
            self.tv_All_Data.delete(*self.tv_All_Data.get_children())
            return None

        frame1 = tk.LabelFrame(self.show_data, text=f"{self.path}")
        frame1.place(height=420, width=768, rely=0.02, relx=0.02)

        self.tv_All_Data = ttk.Treeview(frame1)
        self.tv_All_Data.place(relheight=1, relwidth=1)

        # commande signifie mettre à jour la vue de l'axe y du widget
        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=self.tv_All_Data.yview)

        # commande signifie mettre à jour la vue axe x du widget
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=self.tv_All_Data.xview)

        # affecter les barres de défilement au widget Treeview
        self.tv_All_Data.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)

        # faire en sorte que la barre de défilement remplisse l'axe x du widget Treeview
        treescrollx.pack(side="bottom", fill="x")

        # faire en sorte que la barre de défilement remplisse l'axe y du widget Treeview
        treescrolly.pack(side="right", fill="y")

        global count
        count = 0

        self.tv_All_Data.tag_configure("oddrow", background="white")
        self.tv_All_Data.tag_configure("evenrow", background="#D3D3D3")

        # vider le treeview
        self.tv_All_Data.delete(*self.tv_All_Data.get_children())

        self.tv_All_Data["column"] = list(self.df.columns)
        self.tv_All_Data["show"] = "headings"

        for column in self.tv_All_Data["columns"]:
            self.tv_All_Data.column(column, anchor="w")
            self.tv_All_Data.heading(column, anchor="w", text=column)

        self.df_rows = self.df.to_numpy().tolist()
        for row in self.df_rows:
            if count % 2 == 0:
                self.tv_All_Data.insert(
                    "",
                    "end",
                    iid=count,
                    values=row,
                    tags=("evenrow",),
                )
            else:
                self.tv_All_Data.insert(
                    "",
                    "end",
                    iid=count,
                    values=row,
                    tags=("oddrow",),
                )
            count += 1

        self.tv_All_Data.insert("", "end", values="")

        return None


    def updateState(self):
        self.path, self.df = self.setState()
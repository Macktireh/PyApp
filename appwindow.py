import tkinter as tk

from tkinter import PhotoImage
from components.home import Home


class MainWindow:

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

        self.home = Home(
            root = self.root, 
            excelIcon = self.excelIcon, 
            viewIcon = self.viewIcon,
        ).display()

    def start(self):
        self.root.mainloop()
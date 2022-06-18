import tkinter as tk

from dataclasses import dataclass
from tkinter import PhotoImage
from appwindow import MainWindow


@dataclass
class SplachScreen:
    root: tk.Tk = tk.Tk()
    width: int = 400
    height: int = 200

    def display(self):
        self.root.overrideredirect(True)
        self.root.update_idletasks()

        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = self.width + 2 * frm_width

        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = self.height + titlebar_height + frm_width

        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2

        self.root.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))
        self.root.config(background="#f1f1f1")
        self.root.deiconify()

        self.BtnExit = tk.Label(
            self.root,
            text="  X  ",
            font=("Helvetica", 13),
            fg="black",
            bd=1
        )
        self.BtnExit.place(relx=0.91, rely=0.01)
        self.BtnExit.bind("<Button-1>", self.Exit)

        self.splach_logo = PhotoImage(file="static/img/TotalEnergies.png")
        self.splach_logo = self.splach_logo.subsample(2, 2)

        self.label_show_splach_logo = tk.Label(
            self.root,
            image=self.splach_logo,
            width=150,
            height=150
        ).place(relx=0.32, rely=0.04)

        self.splach_label = tk.Label(
            self.root,
            text="     Data App Desktop",
            font=("Helvetica", 15)
        ).place(relx=0.23, rely=0.7)

        for b in [self.BtnExit]:
            b.bind("<Enter>", self.change_bgcolor)
            b.bind("<Leave>", self.change_fgcolor)

    def Exit(self, e):
        self.root.quit()

    def change_bgcolor(self, e):
        self.BtnExit.config(background="red", fg="white")

    def change_fgcolor(self, e):
        self.BtnExit.config(background="#f1f1f1", fg="black")

    def start(self):
        self.display()
        self.root.after(10000, self.main_window)
        self.root.mainloop()
    
    def main_window(self):
        self.root.destroy()
        MainWindow().start()
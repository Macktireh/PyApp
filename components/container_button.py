import tkinter as tk

from dataclasses import dataclass

@dataclass
class Widget():
    root: tk.Tk
    browse_button: object
    funct: object = None

    def display(self):
        self.FrameBtn = tk.LabelFrame(self.root)
        self.FrameBtn.place(relx=0.02, rely=0.82, relheight=0.15, relwidth=0.96)

        # Button sortie
        self.BtnSortie = tk.Button(
            self.FrameBtn, 
            text="Sortie", 
            font=("Helvetica", 11),
            width=15,
            height=1,
            borderwidth=5,
            relief="raised",
            command=self.browse_button)
        self.BtnSortie.place(relx=0.1, rely=0.2)
        
        # Button Comparer
        self.BtnComparer = tk.Button(
            self.FrameBtn, 
            text="Lancer", 
            font=("Helvetica", 11),
            width=15,
            height=1,
            borderwidth=5,
            relief="raised",
            background="#004C8C",
            activebackground="#004C8C",
            foreground="black",
            activeforeground="white",
            command=self.funct)
        self.BtnComparer.place(relx=0.38, rely=0.2)
        
        # Button Fermer
        self.BtnFermer = tk.Button(
            self.FrameBtn, 
            text="Fermer", 
            font=("Helvetica", 11),
            width=15,
            height=1,
            borderwidth=5,
            relief="raised",
            background="#C60030",
            activebackground="#C60030",
            foreground="black",
            activeforeground="white",
            command=self.root.destroy)
        self.BtnFermer.place(relx=0.65, rely=0.2)
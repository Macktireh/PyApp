import tkinter as tk

from dataclasses import dataclass
from tkinter import messagebox

from actions.import_data import Actions

@dataclass
class Widget():
    root: tk.Tk
    run_compare_files: object = None
    path_export: str = ""

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
            command=self.handle_click_btn_sortie)
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
            command=self.handle_run_compare_files)
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
    
    def handle_click_btn_sortie(self):
        self.path_export = Actions.ask_export_directory(self)
        print(self.path_export)
    
    def handle_run_compare_files(self):
        if self.path_export:
            try:
                self.run_compare_files(self.path_export)
                messagebox.showinfo('Succès', f"Votre fichier de comparaison est prêt.\nEmplacement : {self.path_export}")
            except:
                messagebox.showerror("Information", "Veuiller sélectionner un dossier de sortie correct")
        else:
            messagebox.showerror("Information", "Veuiller sélectionner un dossier de sortie")
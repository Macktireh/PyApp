if True:
    import tkinter as tk
    from tkinter import PhotoImage
    from ui import AppUI


splach_root = tk.Tk()
splach_root.overrideredirect(True)

splach_root.update_idletasks()
width = 400
frm_width = splach_root.winfo_rootx() - splach_root.winfo_x()
win_width = width + 2 * frm_width
height = 200
titlebar_height = splach_root.winfo_rooty() - splach_root.winfo_y()
win_height = height + titlebar_height + frm_width
x = splach_root.winfo_screenwidth() // 2 - win_width // 2
y = splach_root.winfo_screenheight() // 2 - win_height // 2
splach_root.geometry("{}x{}+{}+{}".format(width, height, x, y))
splach_root.config(background="#f1f1f1")
splach_root.deiconify()


def Exit(e):
    splach_root.quit()

def change_bgcolor(e):
   BtnExit.config(background="red", fg="white")

def change_fgcolor(e):
   BtnExit.config(background="#f1f1f1", fg="black")

# , bg="#C60030"
BtnExit = tk.Label(
    splach_root, text="  X  ", font=("Helvetica", 13), fg="black", bd=1)

BtnExit.place(relx=0.91, rely=0.01)
BtnExit.bind("<Button-1>", Exit)

splach_logo = PhotoImage(file="static/img/TotalEnergies.png")
splach_logo = splach_logo.subsample(2, 2)

print_img = tk.Label(splach_root, image=splach_logo, width=150, height=150)
print_img.place(relx=0.32, rely=0.04)

splach_label = tk.Label(
    splach_root, text="     Data App Desktop", font=("Helvetica", 15)
).place(relx=0.23, rely=0.7)


def main_window():
    splach_root.destroy()
    app = AppUI()

for b in [BtnExit]:
   b.bind("<Enter>",change_bgcolor)
   b.bind("<Leave>", change_fgcolor)

splach_root.after(1000, main_window)

tk.mainloop()

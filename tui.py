from tkinter import *
from tkinter import PhotoImage

# #Create an instance of tkinter window
# win = Tk()
# win = "2"
# print(type(win))
# viewIcon = PhotoImage(file="static/img/view.png")
# viewIcon = viewIcon.subsample(50, 50)
# print(type(viewIcon))   
# #Set the geometry of tkinter window
# win.geometry("750x250")
# #Define the style
# style_1 = {'fg': 'black', 'bg': '#C60030', 'activebackground':
# '#C60030', 'activeforeground': 'white'}
# style_2 = {'fg': 'white', 'bg': 'OliveDrab2', 'activebackground':
# 'gray71', 'activeforeground': 'gray71'}
# style_3 = {'fg': 'black', 'bg': 'purple1', 'activebackground':
# 'gray71', 'activeforeground': 'gray71'}
# style_4 = {'fg': 'white', 'bg': 'coral2', 'activebackground':
# 'gray71', 'activeforeground': 'gray71'}
# style_cycle = itertools.cycle([style_1, style_2, style_3, style_4 ])
# #Define a function to update the button style
# def update_style():
#     style = next(style_cycle)
#     button.configure(**style)
# #Create a tk button
# button = Button(win,width=40,font=('Helvetica 18 bold'),text="Change Style", command=update_style)
# button.pack(padx=50, pady=50)
# win.mainloop()


# Changer la couleur bg au survol
"""
# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

def change_bgcolor(e):
   b1.config(background="green3")

def change_fgcolor(e):
   b1.config(background="white")

# Add Buttons to trigger the event
b1=Button(win, text="Hover on Me", font=('Georgia 16'))
b1.pack(pady=60,anchor=CENTER)

# Bind the events
for b in [b1]:
   b.bind("<Enter>",change_bgcolor)
   b.bind("<Leave>", change_fgcolor)

win.mainloop()
"""
# pandas.core.frame.DataFrame

from window import *


myWindow = MainWindow()
myWindow.start()
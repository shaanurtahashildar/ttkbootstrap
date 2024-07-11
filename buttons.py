import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("The Shanur Project")
root.geometry('500x500')
# b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)
#
# b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)
#


# style
my_style = ttk.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 14))
# create button
my_button = ttk.Button(text="click me !!", width=30,
                       bootstyle="success",
                       style="success.Outline.TButton")
my_button.pack(pady=20)



root.mainloop()

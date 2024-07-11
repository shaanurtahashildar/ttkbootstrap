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

# create function for my_button

counter=0
def changer():
    global counter
    counter +=1
    if counter % 2 ==0:
        my_lable_button.config(text="even number")
    else:
        my_lable_button.config(text="odd number")
# create label style
my_lable =ttk.Label(text=" The Project Shanur ", font=("Helvetica", 30),
                    bootstyle ="default, inverse")
my_lable.pack(pady=50)

my_lable_button =ttk.Label(text=" even number ", font=("Helvetica", 30),
                    bootstyle ="default, inverse")
my_lable_button.pack(pady=50)
# create button
my_button = ttk.Button(text="Submit",
                       bootstyle="primary, outline", command=changer)
my_button.pack(pady=20)
root.mainloop()

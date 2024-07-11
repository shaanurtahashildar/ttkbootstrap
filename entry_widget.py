import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("Input/ Entry widget")
root.geometry('500x500')
def speak():
    label.config(text=f"You entered : {data.get()}")

data = ttk.Entry()
data.pack(pady = 50)

text_button = ttk.Button(text="Submit",
                         width=30,
                       bootstyle="success outline", command=speak)
text_button.pack(pady=30)

label = ttk.Label(text="enter data")
label.pack(pady = 30)


root.mainloop()
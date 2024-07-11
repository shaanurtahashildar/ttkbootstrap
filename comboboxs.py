import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("Combo Box's")
root.geometry('500x500')


def clicker():
    lable.config(text=f" You have selected {combo_bx.get()}")

# create bindding function
def click_bind(e):
    lable.config(text=f" You have selected {combo_bx.get()}")
lable = ttk.Label(text="Combo Box",
                font=("Helvetica", 20),
                bootstyle="primary",
                  )
lable.pack(pady=30)

# create dropdown
week_names =["Monday",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday",
             "Saturday",
             "Sunday"]
# create combo box

combo_bx = ttk.Combobox(bootstyle="info", values=week_names)
combo_bx.pack(pady=20)
combo_bx.current(0)
# create button
combo_button= ttk.Button(text="Submit",
                         bootstyle="Success",
                         command=clicker)
combo_button.pack(pady=20)

# bind combo box

combo_bx.bind("<<ComboboxSelected>>", click_bind)
root.mainloop()

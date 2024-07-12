import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("Floodgauge")
root.geometry('700x700')


def starter():
    fldg.start()
def stoper():
    fldg.stop()

def increment():
    fldg.step(10)
    my_lable.config(text=f"you current posision is : {fldg.variable.get()}")
fldg=ttk.Floodgauge(root, bootstyle="success",
                    font=("Helvetica", 18),
                    mask="{}%",
                    maximum=80,
                    orient="horizontal",
                    value=10
                    )
fldg.pack(pady=50, fill=X, padx=20)

start_button = ttk.Button(text="Start",
                          bootstyle="warning, outline",
                          command=starter)
start_button.pack(pady = 30)

stop_button = ttk.Button(text="Stop",
                          bootstyle="Danger, outline",
                          command=stoper)
stop_button.pack(pady = 30)

incrementer = ttk.Button(text="Increment",
                          bootstyle="Info, outline",
                          command=increment)
incrementer.pack(pady = 30)
my_lable =ttk.Label(text=" ", font=("Helvetica", 12),
                    bootstyle ="primary, inverse")
my_lable.pack(pady = 30)

root.mainloop()
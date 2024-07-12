import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("Floodgauge")
root.geometry('500x400')

my_frame = ttk.Frame(bootstyle="light")
my_frame.pack(pady = 40)

data_entry = ttk.Entry(my_frame, font=("Helvetica", 20))
data_entry.pack(pady=20, padx=20)

button = ttk.Button(my_frame, text="Submit" , bootstyle="warning outline")
button.pack(pady=20, padx=20)

label = ttk.Label(text="Hello There......", font=("Helvetica", 18))
label.pack(pady=20)
root.mainloop()
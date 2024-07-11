from  tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("The Shanur Project")
root.geometry('500x500')
#lable
#
# my_lable =ttk.Label(text=" Check buttons", font=("Helvetica", 30),
#                     bootstyle="default, inverse")
# my_lable.pack(pady=50)
#
# def checker():
#     pass
# # checkbutton
#
# var1 = IntVar()
# check_button=ttk.Checkbutton(bootstyle="primary",
#                              text="Check",
#                              variable=var1,
#                              onvalue=1,
#                              offvalue=0,
#                              command=checker)
# check_button.pack(pady=10)

root.mainloop()
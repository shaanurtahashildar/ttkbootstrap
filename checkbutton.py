from  tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")

root.title("The Shanur Project")
root.geometry('500x500')
#lable

my_lable =ttk.Label(text=" Check buttons", font=("Helvetica", 30),
                    bootstyle="default, inverse")
my_lable.pack(pady=50)
ckeck_lable =ttk.Label(text=" Check Status", font=("Helvetica", 30),
                    bootstyle="primary, inverse")
ckeck_lable.pack(pady=(40,10))

def checker():
    if var1.get() == 1:
        ckeck_lable.config(text="Checked", font=("Helvetica", 30),
                    bootstyle="primary")
    else:
        ckeck_lable.config(text="Unchecked", font=("Helvetica", 30),
                           bootstyle="Danger")
# checkbutton

var1 = IntVar()
check_button=ttk.Checkbutton(bootstyle="primary",
                             text="Check",
                             variable=var1,
                             onvalue=1,
                             offvalue=0,
                             command=checker)
check_button.pack(pady=10)

var2=IntVar
check_toolbutton = ttk.Checkbutton(bootstyle="info, toolbutton",
                                   text="Check Tool",
                                   variable=var2,
                                   onvalue=1,
                                   offvalue=0,
                                   command=checker
                                   )
check_toolbutton.pack(pady = 10)

var3=IntVar
check_outlinebutton = ttk.Checkbutton(bootstyle="info, toolbutton, outline",
                                   text="Check outline",
                                   variable=var3,
                                   onvalue=1,
                                   offvalue=0,
                                   command=checker
                                   )
check_outlinebutton.pack(pady = 10)


check_rounttoggle = ttk.Checkbutton(bootstyle="success, round-toggle",
                                   text="round toggle",
                                   variable=var1,
                                   onvalue=1,
                                   offvalue=0,
                                   command=checker
                                   )
check_rounttoggle.pack(pady = 10)

check_squaretoggle = ttk.Checkbutton(bootstyle="warning, square-toggle",
                                   text="square toggle",
                                   variable=var1,
                                   onvalue=1,
                                   offvalue=0,
                                   command=checker
                                   )
check_squaretoggle.pack(pady = 10)

root.mainloop()
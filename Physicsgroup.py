from tkinter import *
from subprocess import call
import tkinter
window=tkinter.Tk()
def clicked():
    call(["python", "Force.py"])
def clicked2():
    call(["python", "Power.py" ])
def clicked3():
    call(["python", "Pressure.py" ])
def clicked4():
    call(["python", "Speed.py" ])
def clicked5():
    call(["python", "velocity.py"])

Button(master=window, text="Force", command=clicked).grid(column=0, row=1)
Button(master=window, text="Power", command=clicked2).grid(column=0, row=2)
Button(master=window, text="Pressure", command=clicked3).grid(column=0, row=3)
Button(master=window, text="Speed", command=clicked4).grid(column=0, row=4)
Button(master=window, text="Velocity", command=clicked5).grid(column=0, row=5)


window.mainloop()
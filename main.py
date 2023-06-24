import tkinter
from tkinter import *
from subprocess import call
window=tkinter.Tk()
def clicked():
    call(["python", "mathsgroup.py"])
def clicked2():
    call(["python", "Physicsgroup.py"])

Button(master=window, text="MATHEMATICS", command=clicked).grid(column=0, row=1)
Button(master=window, text="PHYSICS", command=clicked2).grid(column=0, row=2)


window.mainloop()

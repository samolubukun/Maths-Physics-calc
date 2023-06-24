from tkinter import *
from subprocess import call
import tkinter
window=tkinter.Tk()
def clicked():
    call(["python", "areaoftriangle.py"])
def clicked2():
    call(["python", "areaofrectangle.py" ])
def clicked3():
    call(["python", "areaofsquare.py" ])
def clicked4():
    call(["python", "areaofcircle.py" ])
def clicked5():
    call(["python", "perimeterofsquare.py" ])

Button(master=window, text="Area of triangle", command=clicked).grid(column=0, row=1)
Button(master=window, text="Area of rectangle", command=clicked2).grid(column=0, row=2)
Button(master=window, text="Area of square", command=clicked3).grid(column=0, row=3)
Button(master=window, text="Area of circle", command=clicked4).grid(column=0, row=4)
Button(master=window, text="Perimeter of square", command=clicked5).grid(column=0, row=5)


window.mainloop()
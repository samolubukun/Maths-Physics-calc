from tkinter import *
 
def areaofcircle():
    res=float(22/7)*int(e1.get())*int(e1.get())
    myText.set(res)
 
master = Tk()
myText=StringVar()
Label(master, text="Radius(cm)").grid(row=0, sticky=W),
Label(master, text="Result(cm):").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)

 
e1.grid(row=0, column=1)
 
b = Button(master, text="Calculate", command=areaofcircle)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
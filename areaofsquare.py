from tkinter import *
 
def areaofsquare():
    res=int(e1.get())*int(e2.get())
    myText.set(res)
 
master = Tk()
myText=StringVar()
Label(master, text="Base(cm)").grid(row=0, sticky=W)
Label(master, text="Height(cm)").grid(row=1, sticky=W)
Label(master, text="Result(cm):").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(master, text="Calculate", command=areaofsquare)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
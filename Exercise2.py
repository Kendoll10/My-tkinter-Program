# Lets create a desktop program that converts kilogram to gram, pounds and ounces

from tkinter import *

window = Tk()

def kg_pounds_ounces():
    gram = float(e1_value.get()) * 10000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 32.274
    t1.delete(1.0, END)
    t1.insert(END, gram)
    t2.delete(1.0, END)
    t2.insert(END, pounds)
    t3.delete(1.0, END)
    t3.insert(END, ounces)


b1 = Button(window, text="Convert", command=kg_pounds_ounces)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=2, width = 20)
t1.grid(row=1, column=0)

t2 = Text(window, height=2, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=2, width=20)
t3.grid(row=1, column=2)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

window.mainloop()
# this is a desktop converter app that converts year into seconds, minutes etc...

from tkinter import *

window = Tk()

def years_converter():
    seconds = float(e1_value.get()) * 31536000
    minutes = float(e1_value.get()) * 525600
    hours = float(e1_value.get()) * 8760
    days = float(e1_value.get()) * 365
    weeks = float(e1_value.get()) * 52
    months = float(e1_value.get()) * 12
    t1.delete(1.0, END)
    t1.insert(END, seconds)
    t2.delete(1.0, END)
    t2.insert(END, minutes)
    t3.delete(1.0, END)
    t3.insert(END, hours)
    t4.delete(1.0, END)
    t4.insert(END, days)
    t5.delete(1.0, END)
    t5.insert(END, weeks)
    t6.delete(1.0, END)
    t6.insert(END, months)


b1 = Button(window, text="Converter", command=years_converter)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l0 = Label(window, text="YEAR")
l0.grid(row=0, column=2)

l1 = Label(window, text="SECONDS")
l1.grid(row=1, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)

l2 = Label(window, text="MINUTES")
l2.grid(row=2, column=2)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

l3 = Label(window, text="HOURS")
l3.grid(row=3, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=3, column=1)

l4 = Label(window, text="DAYS")
l4.grid(row=4, column=2)

t4 = Text(window, height=1, width=20)
t4.grid(row=4, column=1)

l5 = Label(window, text="WEEKS")
l5.grid(row=5, column=2)

t5 = Text(window, height=1, width=20)
t5.grid(row=5, column=1)

l6 = Label(window, text="MONTHS")
l6.grid(row=6, column=2)

t6 = Text(window, height=1, width=20)
t6.grid(row=6, column=1)


window.mainloop()
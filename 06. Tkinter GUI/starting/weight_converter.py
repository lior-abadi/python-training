from tkinter import *

window = Tk()

def clearTextBox(textBoxIndicator):
    textBoxIndicator.delete("1.0", "end")

def kg_to_grams():
    grams = float(e1_value.get()) * 1000
    clearTextBox(t1)
    t1.insert(END, grams)

def kg_to_pounds():
    grams = float(e1_value.get()) * 2.20462
    clearTextBox(t2)
    t2.insert(END, grams)

def kg_to_ounces():
    ounces = float(e1_value.get()) * 35.274
    clearTextBox(t3)
    t3.insert(END, ounces)

def convertAll():
    kg_to_grams()
    kg_to_pounds()
    kg_to_ounces()

# Button Object
b1 = Button(text = "Convert", command = convertAll )
b1.grid(row= 0 , column = 2)

# Entry Object
e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row=0 , column=1)

# Text Object
t1 = Text(window, height= 1, width=20)
t1.grid(row= 1 , column = 0)

# Text Object
t2 = Text(window, height= 1, width=20)
t2.grid(row= 1 , column = 1)

# Text Object
t3 = Text(window, height= 1, width=20)
t3.grid(row= 1 , column = 2)

# Label Object
l1 = Label(window, text= "Enter kilograms (kg)")
l1.grid(row= 0 , column = 0)

window.mainloop()
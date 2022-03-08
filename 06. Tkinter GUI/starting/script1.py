from tkinter import *

window = Tk()
window.geometry("450x450")

def clearTextBox(textBoxIndicator):
    textBoxIndicator.delete("1.0", "end")

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    clearTextBox(t1)
    t1.insert(END, miles)

# Button Object
b1 = Button(text = "Excecute", command = km_to_miles)
b1.grid(row= 0 , column = 0)

# Entry Object
e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row=0 , column=1)

# Text Object
t1 = Text(window, height= 1, width=20)
t1.grid(row= 0 , column = 2)



window.mainloop()
'''
This program stores book information:
Title, Author, Year, ISBN.

The User is able to:
View all records
Search an Entry
Add Entry
Update Entry
Delete Entry
Close Window

'''

from tkinter import *
from turtle import back
from backend import Database

database = Database("books.db")


# Usage Functions 
def clearList():
    lb1.delete(0, END)

def refreshList():
    lb1.delete(0, END)
    for row in database.view():
        lb1.insert(END, row)

def view_command():
    lb1.delete(0, END)
    refreshList()

def search_command():
    lb1.delete(0, END)
    for row in database.search(title_text.get(), autor_text.get(), year_text.get(), isbn_text.get()):
        lb1.insert(END, row)

def add_command():
    database.insert(title_text.get(), autor_text.get(), year_text.get(), isbn_text.get())
    lb1.delete(0, END)
    lb1.insert(END, "Successfully added the book.")

def get_selected_row(event):
    global selected_tuple
    if lb1.curselection():
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    
def delete_command():
    database.delete(selected_tuple[0])
    lb1.delete(0, END)
    refreshList()

def update_command():
    database.update(selected_tuple[0], title_text.get(), autor_text.get(), year_text.get(), isbn_text.get())
    lb1.delete(0, END)
    refreshList()


window = Tk()
window.title("BookStore")

# Text Object - TITLE
l1 = Label(window, height= 1, width=20, text = "Title")
l1.grid(row= 0 , column = 0)

# Text Object - AUTHOR
l2 = Label(window, height= 1, width=20, text = "Author")
l2.grid(row= 0 , column = 2)

# Text Object - YEAR
l3 = Label(window, height= 1, width=20, text = "Year")
l3.grid(row= 1 , column = 0)

# Text Object - ISBN
l4 = Label(window, height= 1, width=20, text = "ISBN")
l4.grid(row= 1 , column = 2)


# Entry Object
title_text = StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0 , column=1)

autor_text = StringVar()
e2 = Entry(window, textvariable= autor_text)
e2.grid(row=0 , column=3)

year_text = StringVar()
e3 = Entry(window, textvariable= year_text)
e3.grid(row=1 , column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable= isbn_text)
e4.grid(row=1 , column=3)

# Button Objects
b1 = Button(text = "View All", command = view_command )
b1.grid(row= 3 , column = 3,  sticky="nesw")

b2 = Button(text = "Search Entry", command = search_command)
b2.grid(row= 4 , column = 3,  sticky="nesw")

b3 = Button(text = "Update Selected" , command = update_command)
b3.grid(row= 6 , column = 3, sticky="nesw")

b4 = Button(text = "Delete Selected" , command = delete_command)
b4.grid(row= 7 , column = 3,  sticky="nesw")

b5 = Button(text = "Close" , command = window.destroy)
b5.grid(row= 9 , column = 3,  sticky="nesw")

b6 = Button(text = "Add Entry", command=add_command)
b6.grid(row= 5 , column = 3,  sticky="nesw")

b7 = Button(text = "Clear List" , command = clearList)
b7.grid(row= 8 , column = 3,  sticky="nesw")


# Listbox Object
lb1 = Listbox(window, height= 6 , width= 35)
lb1.grid(row= 2 , column = 0, rowspan= 6, columnspan= 3)

# Scroll bar object
sb1 = Scrollbar(window)
sb1.grid( row=2, column=2, rowspan= 6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command = lb1.yview   )

lb1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()
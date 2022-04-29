# Import Module
from tkinter import *
import sqlite3

def create_db():
    """
    this method will create database if not created
    :return:
    """
    conn = sqlite3.connect('contact.db')
    conn.execute('''CREATE TABLE CONTACTS
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             NUMBER            INT     NOT NULL,
             ADDRESS        CHAR(50);''')
    conn.close()

def add():
    """
    this method will add contact details to the database
    :return:
    """

def view():
    """
    this method will retrieve details for selected contact and show on screen
    :return:
    """
def delete():
    """
    this method will delete contact details of selected contact
    :return:
    """

def create_GUI():
    """
    this method will create GUI for the app
    :return:
    """

    root = Tk()
    root.title("Contact Book")
    root.geometry('400x430')

    Name = StringVar()
    Number = StringVar()

    Label(root, text='Name', font='arial 12 bold').place(x = 10, y = 10)
    Entry(root, textvariable=Name, width=45).place(x = 100, y = 10)

    Label(root, text='Phone No.', font='arial 12 bold').place(x = 10, y = 50)
    Entry(root, textvariable=Number, width=45).place(x = 100, y = 50)

    Label(root, text='Address', font='arial 12 bold').place(x = 10, y = 120)
    address = Text(root, width=30, height=3)
    address.place(x = 100, y = 100)

    Button(root, text="Add", font="arial 12 bold", command=add).place(x=85, y=390)
    Button(root, text="View", font="arial 12 bold", command=view).place(x=145, y=390)
    Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=210, y=390)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12, width  = 60)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=20, y=170)

    # Execute Tkinter
    root.mainloop()


if __name__ == "__main__":
    create_GUI()
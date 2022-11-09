#gui.py

import sqlite3
import os.path
import tkinter as ttk
from tkinter import *
from sqlite3 import Error, connect
from venv import create
from functions import *

con= sqlite3.connect("maindb")
cursor= con.cursor()

if os.path.isfile("maindb") == True:
    print("maindb exists: True")
    print("\n")
else:
    print("maindb not found")

root = Tk()
root.geometry("360x360")
root.title("IMS")
frm = ttk.Frame(root, padx=10,pady=10)
frm.grid()
ttk.Label(frm, text="Welcome to IMS (Inventory Management System)").grid(column=0, row=0)
ttk.Label(frm, text= "What would you like to do?").grid(column=0,row=1)
ttk.Button(frm, text="1: View database",command=fetch_rowids_gui).grid(column=0,row=2)
ttk.Button(frm, text="2: Add to database(s)",command= inputbox).grid(column=0, row=3)
ttk.Button(frm, text="3: Remove from database",command= inputbox).grid(column=0, row=4)
ttk.Button(frm, text="4: Add a new database",command= inputbox).grid(column=0, row=5)
ttk.Button(frm, text="5: Delete an existing database",command= inputbox).grid(column=0, row=6)
ttk.Button(frm, text="6: Search by manufacturer, model, or S/N",command= inputbox).grid(column=0, row=7)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=8)
root.mainloop()


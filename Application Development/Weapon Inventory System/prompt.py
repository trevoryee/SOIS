#prompt.py

import sqlite3
import os.path
from sqlite3 import Error, connect
from venv import create
from functions import *

con= sqlite3.connect("weapondb")
cursor= con.cursor()

if os.path.isfile("weapondb") == True:
    print("Weapondb exists: True")
    print("\n")
else:
    print("Weapondb not found")

create_table()

print("Welcome to WIS")
print("\n")
print("What would you like to do?")
print("1: Add to database")
print("2: View database")
print("3: Remove from database")
prompt= input("Select a number: ")

if prompt == '1':
    inputs()
    infoconfirm= input("Is this correct? (Y/N inputs only): ")
    while infoconfirm.casefold() == 'n':
        inputs()
        infoconfirm= input("Is this correct? (Y/N inputs only): ")
    
        if infoconfirm.casefold() == 'y':
            insert_db()
    insert_db()
    fetch_info()
    con.close()

if prompt == '2':
    fetch_rowids()
    con.close()

if prompt == '3':
    fetch_rowids()
    delete_info_input()
    infoconfirm= input("Are you sure? (Y/N inputs only): ")
    while infoconfirm.casefold() == 'n':
        delete_info()
        infoconfirm= input("Are you sure? (Y/N inputs only): ")
    
        if infoconfirm.casefold() == 'y':
            delete_info()
    fetch_rowids()
    con.close()
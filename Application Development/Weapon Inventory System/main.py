#main.py 
#This application should take input for weapon s/n, mfr and 
#Trevor Yee 10/6/2022

import sqlite3
import os.path
from sqlite3 import Error, connect
from functions import *

con = sqlite3.connect("weapondb")
cursor= con.cursor()

if os.path.isfile("weapondb") == True:
    print("weapondb exists")


create_table()

list_table()

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
#main.py 
#This application should take input for weapon s/n, mfr and 
#Trevor Yee 10/6/2022

import sqlite3
import os.path
from sqlite3 import Error, connect

con = sqlite3.connect("weapondb")
cursor= con.cursor()

if os.path.isfile("weapondb") == True:
    print("weapondb exists")

def create_table():
    try:
        con= sqlite3.connect('weapondb')
        cursor.execute("CREATE TABLE weapons(mfr,model,sn)")
        print("Table 'Weapons' created")
    except Error as e:
        print(e)
    
create_table()

def list_table():
    result= cursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchone())

list_table()

def inputs():
    global mfr
    global model
    global sn
    mfr =  input("Please input the weapon manufacturer: ")
    model= input("Please input the model of the weapon: ")
    sn= input("Please input the serial number of the weapon: ")
    print(mfr, model, sn)


def insert_db():
    cursor.execute("INSERT INTO 'weapons' VALUES (?,?,?)", (mfr, model, sn))
    con.commit()

inputs()

infoconfirm= input("Is this correct? (Y/N inputs only): ")
while infoconfirm.casefold() == 'n':
    inputs()
    infoconfirm= input("Is this correct? (Y/N inputs only): ")
    
    if infoconfirm.casefold() == 'y':
        insert_db()


def fetch_info():
    result= cursor.execute("SELECT * FROM weapons")
    print(result.fetchall())


fetch_info()

con.close()
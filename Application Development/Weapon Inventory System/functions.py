#functions.py

import sqlite3
import os.path
from sqlite3 import Error, connect

con = sqlite3.connect("weapondb")
cursor= con.cursor()

def create_table():
    try:
        con= sqlite3.connect('weapondb')
        cursor.execute("CREATE TABLE weapons(mfr,model,sn)")
        print("Table 'Weapons' created")
    except Error as e:
        print(e)

def list_table():
    result= cursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchone())

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

def fetch_info():
    result= cursor.execute("SELECT * FROM weapons")
    print(result.fetchall())
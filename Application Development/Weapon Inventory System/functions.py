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

def fetch_rowids():
    try:
        sqliteConnection = sqlite3.connect('weapondb')
        print("Connected to SQLite")

        select_query = """SELECT * from weapons"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("ID: ", row[0])
            print("MFR: ", row[0])
            print("Model: ", row[1])
            print("SN: ", row[2])
            print("\n")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def delete_info_input():
    global delete_input
    weapon_id= input("WeaponID: ")
    delete_input= str(weapon_id)
    

def delete_info():
    sqliteConnection = sqlite3.connect('weapons')
    cursor.execute("""DELETE FROM weapons WHERE rowid=?""",(delete_input))
    con.commit()
    
def closecon():
    cursor.close()
#functions.py

import sqlite3
import os.path
from sqlite3 import Error, connect

con = sqlite3.connect("maindb")
cursor= con.cursor()

def create_table():
    try:
        con= sqlite3.connect('maindb')
        cursor.execute("CREATE TABLE weapons(mfr,model,sn)")
        print("Table 'Weapons' created")
    except Error as e:
        print("Table 'weapons' exists")

def create_table_custom():
    try:
        con= sqlite3.connect('maindb')
        tablename= input("Table name: ")
        cursor.execute("CREATE TABLE " + tablename + "(mfr,model,sn)")
    except Error as e:
        print("Table with name",tablename,"exists")

def list_table():
    result= cursor.execute("SELECT name FROM sqlite_master")
    return result.fetchall()

def inputs():
    global mfr
    global model
    global sn
    mfr =  input("Please input the weapon manufacturer: ")
    model= input("Please input the model of the weapon: ")
    sn= input("Please input the serial number of the weapon: ")
    print('Manufacturer: ', mfr,'Model: ', model,'Serial Number: ', sn)

def insert_db():
    activetable= input('What table are you using? ')
    cursor.execute("INSERT INTO " + activetable + " VALUES (?,?,?)", (mfr, model, sn))
    con.commit()

def fetch_info():
    result= cursor.execute("SELECT * FROM weapons")
    print(result.fetchall())

def fetch_rowids():
    try:
        sqliteConnection = sqlite3.connect('maindb')
        print("Connected to SQLite")
        print(list_table())
        activedb= input("Please type your active table: ")
        x= activedb.casefold()
        select_query = "SELECT * from " + x
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            #print("ID: ", row[0])
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
    sqliteConnection = sqlite3.connect('maindb')
    cursor.execute("""DELETE FROM weapons WHERE rowid=?""",(delete_input))
    con.commit()

def deletetable():
    try:
        print(list_table())
        tablename= input("What is the table you want to delete? ")
        x= tablename.casefold()
        cursor.execute("DROP TABLE " + x)
    except Error:
        print(x+ ' does not exist')
    
def closecon():
    cursor.close()
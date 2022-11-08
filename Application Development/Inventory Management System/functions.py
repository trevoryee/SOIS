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
    global activetable
    activetable= input('What table are you using? ')
    mfr =  input("Please input the manufacturer: ")
    model= input("Please input the model: ")
    sn= input("Please input the serial number of the itme: ")
    print('Manufacturer: ', mfr,'Model: ', model,'Serial Number: ', sn)

def insert_db():
    cursor.execute("INSERT INTO " + activetable + " VALUES (?,?,?)", (mfr, model, sn))
    con.commit()

def fetch_info():
    result= cursor.execute("SELECT * FROM "+ activetable)
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
        z= cursor.execute("SELECT ROW_NUMBER() OVER(ORDER BY mfr)RowNum,mfr,model,sn FROM "+x)
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in z:
            print("RowNum: ", row[0])
            print("MFR: ", row[1])
            print("Model: ", row[2])
            print("SN: ", row[3])
            print("\n")

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def delete_info_input():
    global delete_input
    item_id= input("ID: ")
    delete_input= str(item_id)
    

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

def search_table():
    sqliteConnection = sqlite3.connect('maindb')
    print("Connected to SQLite")
    print(list_table())
    activedb= input("Please type your active table: ")
    x= activedb.casefold()
    select_query = "SELECT * from " + x
    cursor.execute(select_query)
    records = cursor.fetchall()
    z= cursor.execute("SELECT ROW_NUMBER() OVER(ORDER BY mfr)RowNum,mfr,model,sn FROM "+x)
    print("Total rows are:  ", len(records))

    def search():
        global search_type
        search_type= input("Input search term (mfr,model,sn): ")
    search()
    while search_type not in ('mfr','model','sn'):
        print('Not valid input')
        search()
    else:
        print('Search type valid')
        
    search_phrase= input("Input "+ search_type +": ")
    search_result= cursor.execute("SELECT * FROM "+ activedb+ " WHERE " + search_type + " = "+ "'" + search_phrase +"'")
    search_success=0
    for i in search_result:
        print(i)
        search_success=1
    if search_success == 0:
        print("No results found")

    

def closecon():
    cursor.close()
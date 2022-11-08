#delete_info

import sqlite3
import os.path
from sqlite3 import Error, connect
from functions import *

con= sqlite3.connect("maindb")
cursor= con.cursor()

fetch_rowids()

delete_info_input()

delete_info()

fetch_rowids()

closecon()
#h04_month.py
#A program to print months and days.
# created by Trevor Yee, 10/5/2022

import zipfile


months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(1):
    x= zip(months,numbers)
    print(tuple(x))
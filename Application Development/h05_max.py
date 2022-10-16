#h05_max.py
# A program to determine the greatest number of 3 provided numbers.
# created by Trevor Yee, 10/13/2022

isnumber= 0

# This function takes input to define n1, n2 and n3.

def number_def():
    global n1, n2, n3
    n1 = input('Define N1: ')
    n2 = input('Define N2: ')
    n3 = input('Define N3: ')
    checknum()

# This function compares the three numbers

def number_compare():
    if (n1 > n2) and (n1 > n3):
        print(n1, "n1 is the max")
    elif n2 > n1 and (n2> n3):
        print(n2, "n2 is the max")
    elif (n3 > n1) and (n3 > n2):
        print(n3, "n3 is the max")
    elif n1 == n2 == n3:
        print("All 3 are equal")
    else:
        print('not worky')

def checknum():
    global isnumber
    try:
        float(n1)
        float(n2)
        float(n3)
        isnumber= 1
    except ValueError:
        print('One, or more, of the three inputs was not a number')
        isnumber= 0

while isnumber == 0:
    number_def()
if isnumber ==1:
    number_compare()
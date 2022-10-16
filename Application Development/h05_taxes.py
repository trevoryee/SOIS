#h05_taxes.py
# A program to calculate taxes
# created by Trevor Yee, 10/13/2022

# This sets the variables 'isnumber' and 'income' so it is defined.
isnumber= 0
income= 0

# This function sets the variable 'income' globally and takes the income.
def incomeinput():
    global income
    income= input("Input yearly income:")

# This function calculates the taxed income.
def calc():
    if fincome <= 10000:
        taxedincome= fincome * 0
        print('Your income is:', fincome,'Tax bracket: 0%',taxedincome)
    elif (fincome >= 10001) and (fincome <= 40000):
        taxedincome=fincome*0.12
        print('Your income is:', fincome,'Tax bracket: 12%','Your due taxes are: ',taxedincome)
    elif (fincome >= 40001) and (fincome <= 80000):
        taxedincome=fincome*0.20
        print('Your income is:', fincome,'Tax bracket: 20%','Your due taxes are: ',taxedincome) 
    elif fincome >= 80001:
        taxedincome=fincome*0.32
        print('Your income is:', fincome, 'Tax bracket: 32%','Your due taxes are: ',taxedincome)

# This function checks if the input was a number
def checknum():
    global isnumber, fincome
    try:
        float(income)
        isnumber= 1
        fincome= float(income)
    except ValueError:
        print(str(income), 'is not a number')
        isnumber= 0

incomeinput()
checknum()

while isnumber == 0:
    incomeinput()
    checknum()
if isnumber == 1:
    calc()
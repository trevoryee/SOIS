#h05_regisration_fees.py
# A program to calculate registration fee.
# created by Trevor Yee, 10/13/2022

isnumber= 0
isvehicle=0

# This function allows input for vehicle type and weight
def vehinfo():
    global vehicle, weightstr
    vehicle= input("Please input the type of vehicle you have (Truck or Car): ")
    weightstr= input("Please input the weight of your vehicle (Must be a number): ")

# This function checks if the weight is a number.
def checknum():
    global isnumber
    try:
        float(weightstr)
        isnumber= 1
    except ValueError:
        print(str(weightstr).title(), 'is not a number')
        isnumber= 0

# This function checks if the input is car, truck or neither.
def checkveh():
    global isvehicle
    if vehicle.casefold() in ('car','truck'):
        isvehicle= 1
    else:
        print('Input not car or truck')
        isvehicle= 0

# This function determines the appropriate fee based on vehicle type and weight
def calc():
    if vehicle.casefold() == 'car' and float(weightstr) < 3000:
        print('Your vehicle is a car weighing', weightstr, 'and the registration fee is 125.00')
    elif vehicle.casefold() == 'car' and float(weightstr) >= 3000:
        print('Your vehicle is a car weighing', weightstr, 'and the registration fee is 200.00')
    elif vehicle.casefold() == 'truck' and float(weightstr) < 4000:
        print('Your vehicle is a truck weighing', weightstr, 'and the registration fee is 250.00')
    elif vehicle.casefold() == 'truck' and float(weightstr) >= 4000:
        print('Your vehicle is a truck weighing', weightstr, 'and the registration fee is 350.00')

vehinfo()
checknum()
checkveh()

# This loops continues if either input is invalid and only calculates the fee once both inputs are valid
while (isnumber == 0) or (isvehicle == 0):
    print("You entered invalid information.")
    vehinfo()
    checknum()
    checkveh()

if (isnumber == 1) and (isvehicle) == 1:
    calc()
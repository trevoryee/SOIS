#h05_regisration_fees.py

def vehinfo():
    global vehicle, weightstr
    vehicle= input("Please input the type of vehicle you have (Truck or Car): ")
    weightstr= input("Please input the weight of your vehicle (Must be a number): ")

def checkinfo():
    global isnumber
    try:
        float(weightstr)
        isnumber= 1
    except ValueError:
        print(weightstr, 'is not a number')
        isnumber= 0

def calc():
    if vehicle.casefold() == 'car' and float(weightstr) < 3000:
        print('Your vehicle is a car weighing', weightstr, 'and the registration fee is 125.00')
    elif vehicle.casefold() == 'car' and float(weightstr) >= 3000:
        print('Your vehicle is a car weighing', weightstr, 'and the registration fee is 200.00')
    elif vehicle.casefold() == 'car' and float(weightstr) < 4000:
        print('Your vehicle is a truck weighing', weightstr, 'and the registration fee is 250.00')
    elif vehicle.casefold() == 'car' and float(weightstr) >= 4000:
        print('Your vehicle is a truck weighing', weightstr, 'and the registration fee is 350.00')


vehinfo()
checkinfo()

while isnumber == 0:
    print("You entered invalid information.")
    vehinfo()
    checkinfo()
if isnumber == 1:
    calc()
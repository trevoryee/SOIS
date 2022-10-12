#h05_regisration_fees.py

vehicle= input("Please input the type of vehicle you have (Truck or Car): ")
weight= float(input("Please input the weight of your vehicle: "))

if vehicle.casefold() == 'car' and weight < 3000:
    print('Your vehicle is a car weighing', weight, 'and the registration fee is 125.00')
elif vehicle.casefold() == 'car' and weight >= 3000:
    print('Your vehicle is a car weighing', weight, 'and the registration fee is 200.00')
elif vehicle.casefold() == 'car' and weight < 4000:
    print('Your vehicle is a truck weighing', weight, 'and the registration fee is 250.00')
elif vehicle.casefold() == 'car' and weight >= 4000:
    print('Your vehicle is a truck weighing', weight, 'and the registration fee is 350.00')
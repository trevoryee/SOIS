# h03_03.py
# A program to slice part of a list
# created by Trevor Yee, 10/2/2022

cars=  ['accord','acura','lexus','audi','jaguar','peugeot','GMC']
cars2= [cars[6]]
cars3= cars[2:5]

cars3.extend(cars2)
print(cars3)
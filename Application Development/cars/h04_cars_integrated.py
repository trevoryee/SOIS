#h04_cars_integrated.py
#This version of cars imports the car list from another file (cars.py) and allows user input on what type of car they want (new or used or both)!
#Trevor Yee 10/6/2022

from cars import *

used_cars= [subaru_impreza, toyota_corolla, honda_accord, ford_f150]

new_cars= [tesla_model]

neworused =  input("Please enter if you want new or used or both: ") #does customer want used or new

if neworused.casefold() == 'used':
    for i in used_cars:
        a= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"]
        print(a.title())

elif neworused.casefold() == 'new':
    for i in new_cars:
        b= "New Car: " + i["make"] + " " + i["model"]+ " Price: " + i["price"]
        print(b.title())

elif neworused.casefold() == 'both':
    for i in used_cars + new_cars:
        if i.get('nou') == 'new' :
            a= "New Car: " + i["make"] + " " + i["model"]+ " Price: " + i["price"]
            print(a.title())
        if i.get('nou') == 'used':
            b= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"] + " Previous Owner: " + i["owner_fname"] + " " + i["owner_lname"]
            print(b.title())

else:
    print('You typed something wrong')
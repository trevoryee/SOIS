#h04_cars_ultra.py

subaru_impreza= {
'owner_lname':'wong',
'owner_fname':'jon',
'model':'impreza',
'make':'subaru',
'price':'7000.00',
'nou':'used'
}
toyota_corolla= {
'owner_lname':'yee',
'owner_fname':'nathaniel',
'model':'corolla',
'make':'toyota',
'price':'3500.00',
'nou':'used'
}

honda_accord={
'owner_lname':'lor',
'owner_fname':'kenny', 
'model':'accord', 
'make':'honda',
'price':'7000.00',
'nou':'used'
}

ford_f150={
'owner_lname':'brady',
'owner_fname':'james',
'model':'f-150',
'make':'ford',
'price':'8500',
'nou':'used'
}

tesla_model={
'owner_lname':'',
'owner_fname':'',
'model':'model s',
'make':'tesla',
'price':'55,000',
'nou':'new'
}

from cars import *

used_cars= [subaru_impreza, toyota_corolla, honda_accord, ford_f150]

new_cars= [tesla_model]

neworused =  input("Please enter if you want new or used or both: ") #does customer want used or new

noustring= str(neworused)

if neworused.casefold() == 'used':
    for i in used_cars:
        a= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"]
        print(a.title())

if neworused.casefold() == 'new':
    for i in used_cars:
        b= "New Car: " + i["make"] + " " + i["model"]+ " Price: " + i["price"]
        print(b.title())

if neworused.casefold() == 'both':
    for i in used_cars + new_cars:
        if i.get('nou') == 'new' :
            a= "New Car: " + i["make"] + " " + i["model"]+ " Price: " + i["price"]
            print(a.title())
        if i.get('nou') == 'used':
            b= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"]
            print(b.title())

else:
    print('You typed something wrong')
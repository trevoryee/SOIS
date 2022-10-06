#h04_cars_integrated.py



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
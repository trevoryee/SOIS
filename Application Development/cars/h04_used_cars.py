#h04_used_cars.py
#Prints info about each car
#Trevor Yee 10/5/2022
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

used_cars= [subaru_impreza, toyota_corolla, honda_accord, ford_f150]

for i in used_cars:
	i= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"] + " Previous Owner: " + i["owner_fname"] + " " + i["owner_lname"] 
	x= str(i)
	print(x.title())
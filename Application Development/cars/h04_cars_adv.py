#h04_cars_adv.py
#A more complicated version of used_cars.py
#Trevor Yee 10/5/2022

from cars import *

used_cars= [subaru_impreza, toyota_corolla, honda_accord, ford_f150]

new_cars= [tesla_model]

for i in used_cars + new_cars:
	if i.get('nou') == 'new' :
		a= "New Car: " + i["make"] + " " + i["model"]+ " Price: " + i["price"]
		print(a.title())
	if i.get('nou') == 'used':
		b= "Used Car: " + i["make"] + " " + i["model"] + " Price: " + i["price"]
		print(b.title())
else:
    print('No cars left to show')
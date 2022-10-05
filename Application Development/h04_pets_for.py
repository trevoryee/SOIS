# h04_pets.py
# A program to remove rats
# created by Trevor Yee, 10/3/2022

pets= ['dog', 'rat', 'koala','cat','rat','panda','goldfish','rat','sloth','rat','rabbit','fish','rat','dolphin']
print("Pets (With rat:"+ str(pets).title())

for item in pets [:]:
    if item == "rat":
        pets.remove("rat")


print("Pets (Without rat):" + str(pets).title())
# h04_pets_for.py
# A program to remove rats, using a 'for' loop
# created by Trevor Yee, 10/3/2022

pets= ['dog', 'rat', 'koala','cat','rat','panda','goldfish','rat','sloth','rat','rabbit','fish','rat','dolphin']
print("Pets (With rat:"+ str(pets).title())

for i in pets [:]:
    if i == "rat":
        pets.remove("rat")


print("Pets (Without rat):" + str(pets).title())
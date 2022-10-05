# h03_01.py
# A program to create a list
# created by Trevor Yee, 09/22/2022

#list
fruits = ['Apple','Orange','Cherry','Peach','Strawberry','Plum','Grapes']
print(fruits)

#append
fruits.append("Guava")
fruits.append("Mango")
fruits.append("Papaya")
print(fruits)

#delete
del fruits[9]
print(fruits)

#pop
popped_fruit= fruits.pop(7)
print("Removed fruit:", popped_fruit)
print("Current fruits:", fruits)
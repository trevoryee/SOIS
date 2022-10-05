# h03_02.py
# A program to print and delete from a list
# created by Trevor Yee, 10/2/2022

my_tuple = ['c','l','a','s','s','350', 'fall', '2022']
n_tuple = ["tuple", [10, 14, 26], (11, 22, 34)]

#print 350
print(my_tuple[5])

#delete fall
print(my_tuple)
del my_tuple[6]
print('my_tuple: "Fall" has been removed from the list')
print(my_tuple)

#print [1][2]
print(n_tuple[1][2])


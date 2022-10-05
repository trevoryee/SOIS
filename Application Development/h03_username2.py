# h03_username2.py
# A program to create a username
# created by Trevor Yee, 10/2/2022

fname =  input("Please enter your first name:")   #firstname
mname= input("Please enter your middle name (if you have no middle name, you may leave it blank):") #middlename
lname= input("Please enter your last name:")   #lastname

name= [fname,mname,lname]

f_initial= name[0][:1]
m_initial=name[1][:1]
l_initials=name[2][:3]

username= (f_initial + m_initial + l_initials).lower()

print('Your username is:' , username)
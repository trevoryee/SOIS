# h03_int_remainder.py
# A program to do division
# created by Trevor Yee, 10/2/2022

dividend =  float(input("Please enter an interger for the dividend:"))   # dividend
divisor= float(input("Please enter an integer for the divisor:")) #divisor
quotient= int(eval('dividend//divisor')) #quotient
remainder= int(eval('dividend%divisor')) #remainder

print('The quotient is:' , quotient)
print('The remainder is:' , remainder)

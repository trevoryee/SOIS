#h05_taxes.py

income= float(input("Input yearly income:"))

if income <= 10000:
    taxedincome= income * 0
    print('Tax bracket: 0%',taxedincome)
elif (income > 10001) and (income < 40000):
    taxedincome=income*0.12
    print('Tax bracket: 12%',taxedincome)
elif (income > 40001) and (income < 80000):
    taxedincome=income*0.20
    print('Tax bracket: 20%',taxedincome) 
elif income > 80001:
    taxedincome=income*0.32
    print('Tax bracket: 32%',taxedincome)
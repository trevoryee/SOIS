#h05_doge_age.py
# A program to calculate dog age.
# created by Trevor Yee, 10/13/2022

isnumber= 0

def set_age():
    global human_age
    human_age= input("Input your dogs age in human years:")

def checknum():
    global isnumber
    try:
        float(human_age)
        isnumber= 1
    except ValueError:
        print('Input(s) was not a number')
        isnumber= 0

def yor():
    global youngdog, olderdog
    youngdog= human_agefloat * 10.5
    olderdog= 21 + (human_agefloat-2) * 4
    if human_agefloat <= 2:
        youngdog= human_agefloat * 10.5
        print("Your dog is under 2, or is 2, in human years and is: ", youngdog, " in dog years")
    elif human_agefloat > 2:
        olderdog= 21 + (human_agefloat-2) * 4
        print("Your dog is over 2 in human years and is: ", olderdog, " in dog years")
    else:
        print("You typed an incorrect number")

while isnumber == 0:
    set_age()
    checknum()
if isnumber ==1:
    human_agefloat= float(human_age)
    yor()
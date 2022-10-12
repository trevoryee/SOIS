#h04_doge_age.py

def set_age():
    global human_age
    human_age= float(input("Input your dogs age in human years:"))

def yor():
    global youngdog, olderdog
    youngdog= human_age * 10.5
    olderdog= 21 + (human_age-2) * 4
    if human_age <= 2:
        youngdog= human_age * 10.5
        print("Your dog is under 2, or is 2, in human years and is: ", youngdog, " in dog years")
    elif human_age > 2:
        olderdog= 21 + (human_age-2) * 4
        print("Your dog is over 2 in human years and is: ", olderdog, " in dog years")
    else:
        print("You typed an incorrect number")

set_age()
yor()
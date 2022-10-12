#h05_max.py



def number_def():
    global n1, n2, n3
    n1 = input('Define N1: ')
    number_check(n1)
    n2 = input('Define N2: ')
    number_check(n2)
    n3 = input('Define N3: ')
    number_check(n3)

def number_compare():
    if (n1 > n2) and (n1 > n3):
        print(n1, "n1 is the max")
    elif n2 > n1 and (n2> n3):
        print(n2, "n2 is the max")
    elif (n3 > n1) and (n3 > n2):
        print(n3, "n3 is the max")
    elif n1 == n2 == n3:
        print("All 3 are equal")
    else:
        print('not worky')

def number_check(input):
    try:
        val= int(input)
        print('Input',input,'is number')
    except ValueError:
        try:
            val=float(input)
            print('Input', input,'is','float')
        except ValueError:
            print(input, 'Not a number')
            print('WARNING, PROGRAM WILL NOT FUNCTION CORRECTLY IF YOU SEE THIS MESSAGE')
        


number_def()
number_compare()
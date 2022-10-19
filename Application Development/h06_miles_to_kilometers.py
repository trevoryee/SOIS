#h06_miles_to_kilometers

def inputs():
    global miles
    miles= input('Enter miles: ')

def checknum():
    global isnumber, float_miles
    try:
        float(miles)
        isnumber= 1
        float_miles= float(miles)
    except ValueError:
        print(str(miles), 'is not a number')
        isnumber= 0
        
def mile_to_kilo():
    global float_miles, kilometers
    kilometers= float_miles * 1.60934
    print(miles,'mile is', kilometers, 'kilometers')

inputs()
checknum()

while isnumber == 0:
    inputs()
    checknum()
if isnumber == 1:
    mile_to_kilo()
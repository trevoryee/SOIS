#h06_wage.py

def wageinput():
    global wage
    wage= input('insert wage: ')

def hourinputs():
    global hours
    hours= input('insert hours: ')

def checknum():
    global isnumber, float_wage, float_hours
    try:
        float(wage)
        float(hours)
        isnumber= 1
        float_wage= float(wage)
        float_hours=float(hours)
    except ValueError:
        print('Wage or hours value is not a number')
        isnumber= 0

def calc():
    global total_wage, overtime
    if float_hours > 40:
        overtime= float_hours-40
        total_wage= (float_wage*40) + (1.5*overtime)
        print('Hourly pay: $', wage)
        print('Hours worked: ', hours, 'hours')
        print('Overtime worked: ', int(overtime), 'hours')
        print('Total wages: $', total_wage)
    if float_hours <= 40:
        total_wage= float_wage*40
        print('Hourly pay: $',wage,)
        print('Hours worked: ', hours, 'hours')
        print('Total wages: $', total_wage)

wageinput()
hourinputs()
checknum()
while isnumber == 0:
    wageinput()
    hourinputs()
    checknum()
if isnumber == 1:
    calc()
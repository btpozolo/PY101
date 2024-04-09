# Isn't it odd
"""
input
    one int
output
    boolean for it the absolute value is odd

problem
    need to first get abs value of int 
    error check that input is int
    edge cases: non int, o 
    0 --> False
    1 --> True
    -1 --> True
    Hi --> 'Please enter an int'

"""

def is_odd(num):
    if type(num) == int:
        return abs(num) % 2 != 0
    else:
        print('Please enter an integer into is_odd')

is_odd(0)
is_odd(-1)
is_odd(1)
is_odd('hi')

# Odd Numbers
for num in range(1, 100, 2):
    print({num})

# Even Numbers
for num in range(2, 101, 2):
    print(num)

# How big is the room
sq_meter_to_feet = 10.7639

def area():
    length = float(input("Please enter the room's length: \n"))
    width = float(input("Please enter the room's width: \n"))
    unit = ''

    if input("If using meters please enter 'y' otherwise enter anything \n") == 'y':
        unit = 'meters'
        area = length * width
        area_in_ft = area * sq_meter_to_feet
    else:
        unit = 'feet'
        area = length * width / sq_meter_to_feet
        area_in_ft = length * width

    print(f"The room's area in meters is: {round(area, 2)} \n"
          f"In feet that is: {round(area_in_ft, 2)}")

area()

#Tip Calculator
bill = float(input('What is the bill? '))
tip = float(input('What is the tip percentage? '))

tip_amt = bill * (tip / 100)

print(f'The tipo is ${tip_amt:.2f} \n'
      f'The total is ${tip_amt + bill:.2f}')
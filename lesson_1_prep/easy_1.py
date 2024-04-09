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

#Sum or Product of Consecutive Integers

def sum_or_prod():
    num = int(input("Please enter an integer greater than 0: "))

    method = input('Enter "s" to compute the sum, or'
                   ' "p" to compute the product. ')
    
    match method:
        case 's':
            for number in range(1, num + 1):
                amount += number
            print(f'The sum of the integers between 1 and {num} is {amount}.')
        case 'p':
            amount = 1
            for number in range(1, num + 1):
                amount *= number
            print(f'The product of the integers between 1 and {num} is {amount}.')
        case _:
            print("Please select 's' or 'p' next time")

sum_or_prod()

# Short Long Short

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2
    
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

# Leap Years (Pt 1)

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year % 100 == 0) and (year % 400 != 0):
        return False
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)


# Leap Year pt 2

def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    else:
        if year % 400 == 0:
            return True
        elif (year % 100 == 0) and (year % 400 != 0):
            return False
        elif (year % 4 == 0) and (year % 100 != 0):
            return True
        else:
            return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

# Multiples of 3 and 5

def multisum(num):
    amount = 0
    for n in range(1, num + 1):
       if (n % 3 == 0) or (n % 5 == 0):
           amount += n
    return amount

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

# UTF-16 String Value

def utf16_value(expression):
    amount = 0
    for letter in expression:
        amount += ord(letter)
    return amount

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
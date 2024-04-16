#1 
def flinstones(num):
    for index in range(0,num):
        print(f'{" " * index}The Flinstones Rock')

flinstones(10)

#2
def factors(number):
    if number < 0:
        print('Please enter a positive value')
        return
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

factors(10)
factors(-10)

#3
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

#5
nan_value = float("nan")

print(nan_value == float("nan"))
print(nan_value)

import math

nan_value = float("nan")

print(math.isnan(nan_value))

#8
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
print(rps('paper'), "rock")
#paper

#10
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
def multiply(num1, num2):
    return num1 * num2

def square(num1):
    return num1 * num1

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# Generalized to power of n function

def power(num1, power = 2):
    prod = 1
    for value in range(power):
        prod = multiply(prod, num1) 
    return prod 

power(3)
def negative(number):
    return (number if number < 1 else -number)


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
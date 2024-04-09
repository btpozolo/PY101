def oddities(lst):
    return (lst[::2])

oddities([2, 3, 4, 5, 6])

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


from random import randrange

age = randrange(20, 101)
print(f'Teddy is {age} years old!')
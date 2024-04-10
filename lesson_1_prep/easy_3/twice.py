def twice(number):
    number = str(number)
    half_upper = len(number) // 2
    div_by_2 = len(number) % 2 == 0
    left_eq_right = number[: half_upper] == number[half_upper: ]
    
    # print(half_upper)
    # print(number[0: half_upper - 1] )
    # print(number[half_upper: len(number) - 1])

    if div_by_2 and left_eq_right:
        return int(number)
    else:
        return int(number) * 2
    
twice(37)

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
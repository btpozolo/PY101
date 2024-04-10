def stringy(num_chars):
    alt_string = ""

    for indx in range(num_chars):
        alt_string += '1' if indx % 2 == 0 else '0'

    return alt_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

def stringy(pos_int):
    recur_times = pos_int // 2

    if pos_int % 2 == 0:
        return "10"*recur_times

    return "10"*recur_times + "1"

stringy(1)
stringy(2)
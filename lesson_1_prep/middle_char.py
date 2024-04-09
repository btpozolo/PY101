def center_of(string):
    num_char = 2 if len(string) % 2 == 0 else 1
    start_index = (len(string) // 2) - 1 if len(string) % 2 == 0 else len(string) // 2
    end_index = start_index + num_char

    return (string[start_index: end_index])

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
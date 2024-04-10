def crunch(old_string):
    new_str = ""

    for index in range(0,len(old_string)):
        add_char = old_string[index] != old_string[index - 1]
        if add_char:
            new_str += old_string[index]
    
    return new_str




# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
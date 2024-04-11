def get_century(year):
    year = str(year)
    num_char = len(year)

    if num_char < 3:
        return 1
    else:
        year_int = int(year)
        cent = year_int // 100 if year_int % 100 == 0 else (year_int // 100) + 1
        return (cent)


def century(year):
    cent = str(get_century(year))
    
    suffix = ""
    
    last_digit = cent[-1]
    
    if len(cent) >= 2:
        second_to_last = cent[-2]

        if second_to_last == '1':
            suffix = 'th'
            return (cent + suffix)


    match last_digit:
        case '1':
            suffix = 'st'
        case '2':
            suffix = 'nd'
        case '3':
            suffix = 'rd'
        case _:
            suffix = 'th'

    return (cent + suffix)

print(century(1965))
print(century(5)) 
print(century(256)) 
print(century(1052)) 
print(century(1127)) 

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

def century(year):
    century_number = year // 100 + 1

    if year % 100 == 0:
        century_number -= 1

    suffix = century_suffix(century_number)
    return f'{century_number}{suffix}'

def century_suffix(century_number):
    last_two = century_number % 100
    last_digit = century_number % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'

    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'
        
print(century(2000) == "20th")     
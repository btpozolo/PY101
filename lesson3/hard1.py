#1
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

#2
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

#3  -- Review
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") #two
print(f"two is: {two}")# three
print(f"three is: {three}") # two

#b
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # one
print(f"two is: {two}") # two
print(f"three is: {three}") # three

#c
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # two
print(f"two is: {two}") # three
print(f"three is: {three}") # one

#4
def is_an_ip_number(num):
    try:
        num = int(num)
        return num in range(0, 256)
    except:
        return False

is_an_ip_number(255)
is_an_ip_number(256)
is_an_ip_number(0)
is_an_ip_number(10)
is_an_ip_number(-255)

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

is_dot_separated_ip_address('12.12.12.12')
is_dot_separated_ip_address('4.5.5')

#5


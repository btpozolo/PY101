#1
numbers = [1, 2, 3, 4]
numbers = []
numbers.clear()
numbers

#4
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[2] = 42
print(my_list1)
print(my_list2)

#5
def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    test = color == "blue" or color == "green"
    return test

is_color_valid('blue')
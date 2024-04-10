def clean_up(string):
    # replace non alpha with space
    new_string = ""
    first_value = "" if string[0].isalnum() else " "
    last_value = "" if string[-1].isalnum() else " "

    for index in range(len(string)):
        new_value = string[index] if string[index].isalnum() else " "
        new_string += new_value

    new_string = new_string.split()
    new_string = first_value + " ".join(new_string) + last_value
    return new_string

print(clean_up("---what's my +*& line?") )

print(clean_up("---what's my +*& line?") == " what s my line ")

my_string = "hello"

for index, character in enumerate(my_string):
    print(f"Index: {index}, Character: {character}")

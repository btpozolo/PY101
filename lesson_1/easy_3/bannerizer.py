def print_in_box(string):
    banner_string = "--"
    break_string = "  "
    for _ in range(len(string)):
        banner_string += '-'
        break_string += ' '
    
    print(f'+{banner_string}+\n'
          f'|{break_string}|\n'
          f'| {string} |\n'
          f'|{break_string}|\n'
          f'+{banner_string}+\n'
          )

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
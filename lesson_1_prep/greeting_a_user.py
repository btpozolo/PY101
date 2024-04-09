def greeting():
    name = input('What is your name? ')
    name = name.strip()

    if name[-1] == '!':
        name = name.strip('!')
        print(f'Hello {name}! why are we yelling?'.upper())
    else:
        print(f'Hello {name}.')

greeting()
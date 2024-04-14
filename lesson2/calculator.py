import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def run_calc():
    prompt(MESSAGES['first_num'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_num'])
        number1 = input()

    prompt(MESSAGES['second_num'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4', ]:
        prompt(MESSAGES['invalid_op'])
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(f"The result is: {output:.2f}")


prompt(MESSAGES['welcome'])

while True:
    run_calc()
    prompt(MESSAGES['run_again'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
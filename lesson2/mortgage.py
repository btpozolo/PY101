def prompt(message):
    print(f'==> {message}')

def get_input(message):
    prompt(message)
    return input()

def invalid_num(entry):
    try:
        float(entry)
    except ValueError:
        prompt(f'Sorry the number you entered ({entry}) is not valid')
        return True
    if float(entry) > 0:
        return False
    return True

def stop_program():
    return (get_input('Would you like to run program again? [y/n]')
            .strip().lower() != 'y')

def run_calculator():
    loan_amount = get_input('Please enter the total loan amount')

    while invalid_num(loan_amount):
        loan_amount = get_input('Please re-enter a loan amount in '
                                'positive number in format (##.##):')

    prompt('Please enter the APR:')
    apr = get_input('example format: 5 = 5%')

    while invalid_num(apr):
        apr = get_input('Please re-enter an APR as a positive integer')

    duration_years = get_input('Please enter the loan duration in positive '
                               'number of years:')

    while invalid_num(duration_years):
        duration_years = get_input('Please re-enter an APR as a positive '
                                   'integer')

    # Calculate loan payment
    apr_in_months = float(apr) / 12
    duration_in_months = float(duration_years) * 12
    monthly_payment = (float(loan_amount) * (apr_in_months /
                        (1 - (1 + apr_in_months) ** (-duration_in_months))))

    # Output monthly payment
    print(f'==> The monthly payment on the loan is ${monthly_payment:,.2f}\n'
        f'==> with {duration_in_months:,.0f} total payments to make.')

prompt('Welcome to the payment builder!')
while True:
    run_calculator()
    print('---------------------------------------------')
    print()
    if stop_program():
        prompt('Thank you for using the payment calculator!')
        break
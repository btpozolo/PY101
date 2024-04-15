import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock', ]
SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'p']
FULL_CHOICES = [[x, y] for x, y in zip(VALID_CHOICES, SHORTENED_CHOICES)]

player_score = {
        'User':     0,
        'Computer': 0,
}
player_keys = list(player_score.keys())

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def display_winner(user_choice, computer_choice):
    prompt(f"You chose {user_choice}, computer chose {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == player_keys[0]:
        prompt("You win!")
    elif winner == player_keys[1]:
        prompt("Computer wins!")
    else:
        prompt("Its a tie!")

def prompt(message):
    print(f"==> {message}")

def convert_choice(choice):
    if len(choice) == 1:
        for item in FULL_CHOICES:
            if item[1] == choice:
                choice = item[0]
    return choice

def get_choice():
    temp_choice = input()
    choice = convert_choice(temp_choice)

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        prompt(list(FULL_CHOICES))
        temp_choice = input()
        choice = convert_choice(temp_choice)

    return choice

def display_welcome():
    print('\n----------------------------------------------\n'
        '--------- Welcome to RPS Game ----------------\n'
        '----------------------------------------------\n')

def play_round():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    prompt(list(FULL_CHOICES))
    choice = get_choice()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)
    increment_score(get_winner(choice, computer_choice))

def increment_score(player):
    if player in player_score:
        player_score[player] += 1

def get_winner(user_choice, computer_choice):
    if computer_choice in WINNING_COMBOS[user_choice]:
        return player_keys[0] # Player wins
    if user_choice == computer_choice:
        return 'tie'
    return player_keys[1] # Computer wins

def play_again():
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while not (answer.startswith('n') or answer.startswith('y')):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        return False
    return True

def is_grand_winner():
    return max(player_score.values()) >= 3

def get_grand_winner():
    return max(player_score, key = player_score.get)

def display_scores():
    for key, value in player_score.items():
        prompt(f'{key} has a score of: {value}')
    print('')

# Main Program
display_welcome()

while True:

    while is_grand_winner() is not True:
        play_round()
        display_scores()

    print(f'The grand winner is {get_grand_winner()}!\n')

    if not play_again():
        prompt('Thank you for playing!')
        break

    for name in player_score:
        player_score[name] = 0
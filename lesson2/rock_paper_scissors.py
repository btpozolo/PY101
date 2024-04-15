import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock', ]
SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'p']
FULL_CHOICES = [[x, y] for x, y in zip(VALID_CHOICES, SHORTENED_CHOICES)]
PLAYER_TYPE = ['user', 'computer']

# user_score = 0
# computer_score = 0

def display_winner(user_choice, computer_choice):
    prompt(f"You chose {user_choice}, computer chose {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == PLAYER_TYPE[0]:
        prompt("You win!")
    elif winner == PLAYER_TYPE[1]:
        prompt("Computer wins!")
    else:
        prompt("Its a tie!")

def prompt(message):
    print(f"==> {message}")

def convert_choice(choice):
    if len(choice) == 1:
        for item in FULL_CHOICES:
            #print(item)
            if item[1] == choice:
                #print(item[1])
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
    if player == PLAYER_TYPE[0]:
        nonlocal user_score += 1
    elif player == PLAYER_TYPE[1]:
        nonlocal computer_score += 1

def get_winner(user_choice, computer_choice):
    if ((user_choice == "rock" and (computer_choice == "scissors" or 
            computer_choice == 'lizard')) or
        (user_choice == "paper" and (computer_choice == "rock" or 
            computer_choice == 'spock')) or
        (user_choice == "scissors" and (computer_choice == "paper" or 
            computer_choice == 'lizard')) or
        (user_choice =='lizard' and (computer_choice == 'paper' or 
            computer_choice == 'spock')) or
        (user_choice == 'spock' and (computer_choice == 'rock' or 
            computer_choice == 'scissors'))
        ):
        return PLAYER_TYPE[0]
    elif user_choice == computer_choice:
        return 'tie'
    else:
        return PLAYER_TYPE[1]

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
    return max(user_score, computer_score) >= 3

def get_grand_winner():
    if user_score > computer_score:
        return PLAYER_TYPE[0]
    return PLAYER_TYPE[1]

# Main Program
display_welcome()

while True:
    user_score = 0
    computer_score = 0

    while is_grand_winner() != True:
        play_round()

    print(f'The grand winner is {get_grand_winner()}!')

    if not play_again():
        prompt('Thank you for playing!')
        break

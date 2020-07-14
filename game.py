import random


pairs = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}


def print_rps_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
    elif pairs[user_choice] == computer_choice:
        print(f'Sorry, but computer chose ({computer_choice})')
    else:
        print(f'Well done. Computer chose {computer_choice} and failed)')


while True:
    user_choice = input()

    if user_choice == '!exit':
        print('Bye!')
        break

    if user_choice not in pairs:
        print('Invalid input')
        break

    computer_choice = random.choice(list(pairs.keys()))
    print_rps_result(user_choice, computer_choice)



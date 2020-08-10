import random
import math

default_options = ['paper', 'scissors', 'rock']
result = {
    'win': {
        'text': 'Well done. Computer chose {computer_choice} and failed',
        'points': 100
    },
    'draw': {
        'text': 'There is a draw ({computer_choice})',
        'points': 50
    },
    'losing': {
        'text': 'Sorry, but computer chose ({computer_choice})',
        'points': 0
    }
}


def print_rps_result(result_win, computer_choice):
    result_info = result.get(result_win)
    print(result_info['text'].format(computer_choice=computer_choice))


def who_win(user_choice, computer_choice, user_options):
    if user_choice == computer_choice:
        return 'draw'
    elif computer_choice in user_options[user_choice]:
        return 'win'
    else:
        return 'losing'


def get_user():
    user = input('Enter your name: ')
    print(f'Hello, {user}')
    return user


def get_rating(user):
    rating_file = open('rating.txt', 'r')
    users_list = rating_file.readlines()
    rating_file.close()

    rating = 0
    for user_score in users_list:
        name, score = user_score.split(' ')
        if name == user:
            rating = int(score)
            break
    return rating


def prepare_options(user_options):
    length = len(user_options)
    half = math.ceil((length - 1) / 2)

    user_options = user_options * 3
    result = {}
    for i in range(length):
        result[user_options[i]] = user_options[length + i - half:length + i]
    return result


def get_options():
    user_options = input().lower()
    user_options = user_options.split(',') if user_options != '' else default_options
    return prepare_options(user_options)


user_name = get_user()
user_score = get_rating(user_name)
options = get_options()

print("Okay, let's start")
while True:
    user_choice = input()

    if user_choice == '!exit':
        print('Bye!')
        break
    elif user_choice == '!rating':
        print(f'Your rating: {user_score}')
    elif user_choice in options:
        computer_choice = random.choice(list(options.keys()))
        game_result = who_win(user_choice, computer_choice, options)
        user_score += result.get(game_result)['points']
        print_rps_result(game_result, computer_choice)
    else:
        print('Invalid input')

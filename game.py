import random

pairs = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
result = {
    'win': {
        'text': 'Well done. Computer chose {computer_choice} and failed)',
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


def who_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif pairs[user_choice] == computer_choice:
        return 'losing'
    else:
        return 'win'


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


user_name = get_user()
user_score = get_rating(user_name)
while True:
    user_choice = input()

    if user_choice == '!exit':
        print('Bye!')
        break
    elif user_choice == '!rating':
        print(f'Your rating: {user_score}')
    elif user_choice in pairs:
        computer_choice = random.choice(list(pairs.keys()))
        game_result = who_win(user_choice, computer_choice)
        user_score += result.get(game_result)['points']
        print_rps_result(game_result, computer_choice)
    else:
        print('Invalid input')

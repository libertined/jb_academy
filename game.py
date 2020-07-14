import random


pairs = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}

user_choice = input()
computer_choice = random.choice(list(pairs.keys()))

if user_choice == computer_choice:
    print(f'There is a draw ({user_choice})')
elif pairs[user_choice] == computer_choice:
    print(f'Sorry, but computer chose ({computer_choice})')
else:
    print(f'Well done. Computer chose {computer_choice} and failed)')

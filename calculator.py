# write your code here

while True:
    command = input()
    if command == '/exit':
        print('Bye!')
        break
    elif command == '/help':
        print('The program calculates the sum of numbers')
        continue
    elif command == '':
        continue

    numbers = [int(x) for x in command.split(' ')]
    print(sum(numbers))

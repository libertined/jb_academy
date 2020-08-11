# write your code here

while True:
    command = input()
    if command == '/exit':
        print('Bye!')
        break
    numbers = command.split(' ')
    if len(numbers) == 1 and numbers[0] != '':
        print(numbers[0])
    elif len(numbers) == 2:
        print(int(numbers[0]) + int(numbers[1]))

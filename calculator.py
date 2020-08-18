# write your code here
def get_digit(number):
    return int(number.replace(' ', ''))


def get_numbers(input_string):
    result = []
    number = ''
    for i in input_string:
        if i == '+':
            if number == '-':
                continue
            elif number != '':
                result.append(get_digit(number))
                number = ''
            continue
        elif i == '-':
            if number == '-':
                number = ''
                continue
            elif number != '':
                result.append(get_digit(number))
                number = ''
        number += i
    if number != '':
        result.append(get_digit(number))
    return result


while True:
    command = input()
    if command == '/exit':
        print('Bye!')
        break
    elif command == '/help':
        print('The program calculates the sum of positive and negative numbers')
        continue
    elif command == '':
        continue

    numbers = get_numbers(command)
    print(sum(numbers))

from typing import Dict


class Recipe:

    def __init__(self, water, milk, beans, price):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price


class CoffeeMachine:
    action_list = ["buy", "fill", "take", "remaining"]
    recipe_list = {
        "1": Recipe(250, 0, 16, 4),  # espresso
        "2": Recipe(350, 75, 20, 7),  # latte
        "3": Recipe(200, 100, 12, 6),  # cappuccino
    }

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.stage = None
        self.step = None

    def do_action(self, input_str=''):
        if self.stage == "buy":
            self.buy(input_str)
        elif self.stage == "fill":
            self.fill(input_str)
        elif self.stage == "take":
            self.take(input_str)
        elif self.stage == "remaining":
            self.remaining()
        elif self.stage is None:
            self.welcome()

    def init_action(self, input_str):
        if input_str == 'exit':
            return False
        if self.stage is None and len(input_str) > 0:
            self.stage = input_str
            input_str = ''

        self.do_action(input_str)
        return True

    def welcome(self):
        self.step = None
        self.step = None
        print('Write action (buy, fill, take, remaining, exit):')

    def remaining(self):
        result_string = (f'The coffee machine has:\n'
                         f'{self.water} of water\n'
                         f'{self.milk} of milk\n'
                         f'{self.beans} of coffee beans\n'
                         f'{self.cups} of disposable cups\n'
                         f'{self.money} of money\n'
                         )
        print(result_string)
        self.welcome()

    def buy(self, input_str):
        if len(input_str) <= 0:
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        else:
            self.get_coffee(input_str)
            self.welcome()

    def check_quantity(self, recipe):
        if self.cups < 1:
            print('Sorry, not enough cup!')
            return False
        elif self.water < recipe.water:
            print('Sorry, not enough water!')
            return False
        elif recipe.milk < self.milk:
            print('Sorry, not enough milk!')
            return False
        elif self.beans < recipe.beans:
            print('Sorry, not enough coffee beans!')
            return False

        return True

    def make_coffee(self, recipe):
        self.water -= recipe.water
        self.milk -= recipe.milk
        self.beans -= recipe.beans
        self.cups -= 1
        self.money += recipe.money

    def get_coffee(self, recipe_number):
        recipe = self.recipe_list.get(recipe_number)
        if recipe is None:
            return
        if self.check_quantity(recipe):
            print('I have enough resources, making you a coffee!')
            self.make_coffee(recipe)

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        self.welcome()

    def fill_ingredient(self, input_str):
        if len(input_str) <= 0:
            return
        if self.step == 1:
            self.water += int(input_str)
        elif self.step == 2:
            self.milk += int(input_str)
        elif self.step == 3:
            self.beans += int(input_str)
        elif self.step == 4:
            self.cups += int(input_str)

        self.step += 1

    def get_fill_question(self):
        if self.step == 1:
            print('Write how many ml of water do you want to add:')
        elif self.step == 2:
            print('Write how many ml of milk do you want to add:')
        elif self.step == 3:
            print('Write how many grams of coffee beans do you want to add:')
        elif self.step == 4:
            print('Write how many disposable cups of coffee do you want to add:')
        else:
            self.welcome()

    def fill(self, input_str):
        if self.step is None:
            self.step = 1

        self.fill_ingredient(input_str)
        self.get_fill_question()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.welcome()

result = True
while result:
    result = coffee_machine.init_action(input())

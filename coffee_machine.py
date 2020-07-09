from typing import Dict

recipes = {
    "espresso": {"water": 250, "milk": 0, "beans": 16, "price": 4},
    "latte": {"water": 350, "milk": 75, "beans": 20, "price": 7},
    "cappuccino": {"water": 200, "milk": 100, "beans": 12, "price": 6}
}
ingredients: Dict[str, int] = {"water": 1200, "milk": 540, "beans": 120, "cups": 9, "money": 550}
programs = {"1": "espresso", "2": "latte", "3": "cappuccino"}
INGREDIENT_DESC = '''The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money'''


def print_ingredients():
    print(INGREDIENT_DESC.format(water=ingredients["water"],
                                 milk=ingredients["milk"],
                                 beans=ingredients["beans"],
                                 cups=ingredients["cups"],
                                 money=ingredients["money"]))


def get_recipe(coffee_type):
    program = programs.get(coffee_type)
    if program is not None:
        return recipes.get(program)
    else:
        return None


def buy_portion(recipe):
    global ingredients
    ingredients["water"] -= recipe.get("water")
    ingredients["milk"] -= recipe.get("milk")
    ingredients["beans"] -= recipe.get("beans")
    ingredients["cups"] -= 1
    ingredients["money"] += recipe.get("price")


def validate_quantity(recipe):
    if ingredients.get("cups") < 1:
        return False

    if recipe.get("water") <= ingredients.get("water") and \
            recipe.get("milk") <= ingredients.get("milk") and \
            recipe.get("beans") <= ingredients.get("beans"):
        return True
    else:
        return False


def action_buy():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: 3")
    recipe = get_recipe(coffee_type)
    if recipe is None:
        print("There isn't this coffee type")
        return False

    if not validate_quantity(recipe):
        print("There isn't enough ingredients")
        return False

    buy_portion(recipe)


def action_fill():
    global ingredients
    ingredients["water"] += int(input("Write how many ml of water do you want to add: "))
    ingredients["milk"] += int(input("Write how many ml of milk do you want to add: "))
    ingredients["beans"] += int(input("Write how many grams of coffee beans do you want to add: "))
    ingredients["cups"] += int(input("Write how many disposable cups of coffee do you want to add: "))


def action_take():
    global ingredients
    ingredients["money"] = 0
    print("I gave you ${money}".format(money=ingredients["money"]))


print_ingredients()
action = input("Write action (buy, fill, take): ")
if action == "buy":
    action_buy()
elif action == "fill":
    action_fill()
elif action == "take":
    action_take()

print_ingredients()

from math import ceil as roundup


class Recipe:
    def __init__(self, product, ingredients):
        self.ingredients = {}
        for ingr in ingredients:
            amount, name = ingr.split(' ')
            self.ingredients[name] = int(amount)
        self.min_amount, self.name = product.split(' ')
        self.min_amount = int(self.min_amount)

    def __repr__(self):
        # return '{} => {} {}'.format(self.ingredients, self.min_amount, self.name)
        return self.name


input_path = './input.txt'
recipes_input = open(input_path, 'r').read().split('\n')
recipes = dict()
recipes['ORE'] = Recipe('1 ORE', [])
for recipe in recipes_input:
    ingr, product = recipe.split(' => ')
    ingr = ingr.split(', ')
    recipes[product.split(' ')[-1]] = Recipe(product, ingr)


def produce_fuel(amount=1):
    needed_materials = {recipes['FUEL']: amount}
    leftovers_materials = {}
    materials_queue = [recipes['FUEL']]
    while len(materials_queue):
        product = materials_queue.pop(0)
        leftovers = leftovers_materials[product] if product in leftovers_materials else 0
        product_amount = needed_materials[product] - leftovers
        reactions_amount = roundup(product_amount / product.min_amount)
        leftovers_materials[product] = reactions_amount * product.min_amount - product_amount
        for name, amount in product.ingredients.items():
            if recipes[name] in needed_materials:
                needed_materials[recipes[name]] += amount * reactions_amount
            else:
                needed_materials[recipes[name]] = amount * reactions_amount
                materials_queue.append(recipes[name])
        # reset material needed
        if product.name != 'ORE':
            del needed_materials[product]
    return needed_materials[recipes['ORE']]


ores_for_fuel = produce_fuel()
print('answer for part1 is: ', ores_for_fuel)

ores_deposit = 1000000000000
fuels_min = 1
last_fuels = 0
fuels_max = 100000000
while True:
    fuels_mid = int((fuels_min + fuels_max) / 2)
    ores = produce_fuel(fuels_mid)
    if ores < ores_deposit:
        fuels_min = fuels_mid
    elif ores > ores_deposit:
        fuels_max = fuels_mid
    else:
        break
    if last_fuels == fuels_mid:
        break
    else:
        last_fuels = fuels_mid
print('answer for part2 is: ', fuels_min)

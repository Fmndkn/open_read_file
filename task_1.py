from pprint import pprint
import os

def open_book(path):
    with open(path , 'rt', encoding='utf-8') as f:
        result = {}
        for recipes in f:
            recipes_name = recipes.strip()
            count = int(f.readline().strip())
            ingredients = []
            for i in range(count):
                name, quantity, unit = f.readline().split('|')
                item = {
                    'name': name.strip(),
                    'quantity': int(quantity.strip()),
                    'measure': unit.strip(),
                }
                ingredients.append(item)
            result[recipes_name] = ingredients
            f.readline()
    
    return result

def main():
    path = os.path.join(os.getcwd(), 'Python', 'recipes.txt')
    cook_book = open_book(path)
    
    return cook_book

pprint(main())
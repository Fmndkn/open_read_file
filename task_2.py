from pprint import pprint
import os

def open_book(patch):
    with open(patch , 'rt', encoding='utf-8') as f:
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

def count_quantity(cook_book, person_count, result):
    for menu in cook_book:
        name = menu['name']
        if name in result:
            result[name]['quantity'] += menu['quantity']*person_count
        else:
            result[name] = {
                'measure': menu['measure'],
                'quantity': menu['quantity']*person_count
            }
    
    return result

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    cook_book = {}
    patch = os.path.join(os.getcwd(), 'Python', 'recipes.txt')
    cook_book = open_book(patch)
    
    for i in range(len(dishes)):
        if dishes[i] in cook_book:
            result = count_quantity(cook_book[dishes[i]], person_count, result)

    return result

dishes = ['Запеченный картофель', 'Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)

pprint(shop_list)
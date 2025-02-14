def read_recipes(textfile):
    cook_book = {}

    try:
        with open(textfile, 'r', encoding='utf-8') as file:
            while True:
                dish_name = file.readline().strip()

                if not dish_name:
                    break

                ingredient_count = int(file.readline().strip())

                ingredients = []

                for i in range(ingredient_count):
                    ingredient_line = file.readline().strip()

                    ingredient, quantity, measure = ingredient_line.split('|')

                    ingredient_info = {
                        'ingredient_name': ingredient.strip(),
                        'quantity': int(quantity.strip()),
                        'measure': measure.strip()
                    }

                    if ingredient_info['measure'] == 'шт':
                        ingredient_info['measure'] = 'шт.'

                    ingredients.append(ingredient_info)

                cook_book[dish_name] = ingredients

    except FileNotFoundError:
        print("Файл не найден!")
        return {}

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
    return shop_list

def print_formatted_shop_list(shop_list):
    print("{")
    for ingredient, details in shop_list.items():
        print(f"  '{ingredient}': {details},")  
    print("}")


textfile = 'recipes.txt'
cook_book = read_recipes(textfile)


if cook_book:  
    dishes = ['Запеченный картофель', 'Омлет']  
    person_count = 2  

    shopping_list = get_shop_list_by_dishes(dishes, person_count, cook_book)  
    print_formatted_shop_list(shopping_list) 
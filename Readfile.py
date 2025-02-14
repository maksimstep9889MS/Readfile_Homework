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

def print_cook_book(cook_book):
    for dish, ingredients in cook_book.items():
        print(f"  '{dish}': [")
        ingredient_strings = [
            f"    {{'ingredient_name': '{ing['ingredient_name']}', 'quantity': {ing['quantity']}, 'measure': '{ing['measure']}'}}"
            for ing in ingredients
        ]
        print(',\n'.join(ingredient_strings))
        print(" ],")

textfile= 'recipes.txt'
cook_book = read_recipes(textfile)

print_cook_book(cook_book)
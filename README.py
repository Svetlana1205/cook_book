def read_recipes(file_name):
    cook_book = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredients_count):
                ingredient_list = file.readline().strip().split('|')
                ingredients.append({
                    'ingredient_name': ingredient_list[0],
                    'quantity': int(ingredient_list[1]),
                    'measure': ingredient_list[2]
                })
            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено в cook_book!")
    return shop_list


file_name = 'recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)

res_for_10 = get_shop_list_by_dishes(['Блины'], 10, cook_book)
print(res_for_10)











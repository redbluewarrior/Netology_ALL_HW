import os

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    recipes_list = [line.rstrip() for line in recipes]
    while '' in recipes_list:
        recipes_list.remove('')
    #print(recipes_list)
    ingredient_count = 0

    for foods in recipes_list:
        one_food_recipe = []
        ingredient_count += 1

        if ingredient_count == 1:
            food_name = foods
            cook_book[food_name] = []
        elif ingredient_count == 2:
            ingredient_amount = int(foods)
        else:
            foods = foods.split(' | ')
            ingredients = {}
            count_ingredients = 0
            for food in foods:
                count_ingredients += 1
                if count_ingredients == 1:
                    ingredients['ingredient_name'] = food
                if count_ingredients == 2:
                    ingredients['quantity'] = int(food)
                if count_ingredients == 3:
                    ingredients['measure'] = food

            cook_book[food_name].append(ingredients)
            ingredient_amount -= 1

            if ingredient_amount == 0:
                ingredient_count = 0

                
# print(cook_book)

def get_shop_list_by_dishes(dishes=None, person_count=0):
    if dishes is None:
        dishes = []

    guests_dish_ingredients = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                # СОЗДАЕМ КОПИЮ словаря ингредиента, а не используем ссылку
                ingredient_copy = ingredient.copy()

                product = ingredient_copy['ingredient_name']
                quantity = ingredient_copy['quantity'] * person_count

                if product not in guests_dish_ingredients:

                    ingredient_copy['quantity'] = quantity
                    ingredient_name = ingredient_copy.pop('ingredient_name')
                    guests_dish_ingredients[product] = ingredient_copy
                else:
                    # Если ингредиент уже есть, увеличиваем количество
                    guests_dish_ingredients[product]['quantity'] += quantity

    return guests_dish_ingredients


# Тестирование
guests_dish_ingredients = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет'], 4)
print(guests_dish_ingredients)
guests_dish_ingredients = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
print(guests_dish_ingredients)
#print(cook_book)


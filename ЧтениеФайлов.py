
#Задание 1
import os
import datetime
current = os.getcwd()
folder_name = 'my_folder'
file_name = 'recipes.txt'
full_path = os.path.join(current, folder_name, file_name)

with open(full_path, 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        food_name = line.strip()
        ingredient_count = int(file.readline())
        dishes = []
        for i in range(ingredient_count):
           line_with_info = file.readline().strip()
           ingridient_name, quantity, measure = line_with_info.split(' | ')
           dishes.append({'ingridient_name': ingridient_name,
                          'quantity': quantity,
                          'measure': measure})
        file.readline()
        cook_book[food_name] = dishes

#Задание 2
dishes = list()
dishes.append('Омлет')
dishes.append('Фахитос')

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        print(dish)


get_shop_list_by_dishes(dishes, 5)

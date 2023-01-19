
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
        for ingridient in cook_book[dish]:
            key = ingridient['ingridient_name']
            if key in result:
                old = result[key]
                new_quantity = int(ingridient['quantity']) + int(old['quantity'])
                result[key] = {'measure': ingridient['measure'], 'quantity': new_quantity}
            else:
                result[key] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity']}

    #print(result)
get_shop_list_by_dishes(dishes, 5)


#Задание 3

current = os.getcwd()
folder_name = 'my_folder'

result = {}
i = 1
while i <= 3:
    current_file_name = str(i)+'.txt'
    full_path = os.path.join(current, folder_name, current_file_name)
    file = open(full_path, 'r', encoding='utf-8')
    text_in_file = file.read().strip()
    file.close()
    line_count = sum(1 for line in text_in_file)
    result[line_count] = {'file_name': current_file_name, 'text_in_file': text_in_file}
    i = i + 1

result = sorted(result.items())
result = dict(result)
finish_text = ''

for file_info in result.keys():
    line_count = file_info
    file_name = result[file_info]['file_name']
    text_in_file = result[file_info]['text_in_file']
    finish_text = finish_text + str(file_name) + '\n' + str(line_count) + '\n' + str(text_in_file) + '\n\n'

save_time = datetime.datetime.now()
save_time = save_time.date()
result_file_name = 'result_' + str(save_time) + '.txt'
full_path = os.path.join(current, folder_name, result_file_name)
file_result = open(full_path, 'w', encoding='utf-8')
file_result.write(finish_text)
file_result.close()

# Квадраты всех переданных аргументов
import datetime


def sqrt(*args, keyword):
    result = []
    for arg in args:
        result.append(arg ** keyword)
    return result


def decorator_function(func):
    def wrapper(list, param):
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        return func(list, param)
        print('Выходим из обёртки')
    return wrapper

# написать функцию, которая на вход принимает список из целых чисел,
# и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)

@decorator_function
def even_noteven_numbers(list, param):
    new_list = []
    if param == 'четные':
        for element in list:
            if element % 2 == 0:
                new_list.append(element)
    elif param == 'нечетные':
        for element in list:
            if element % 2 > 0:
                new_list.append(element)
    return new_list

a = sqrt(1, 2, 3, 4, keyword = 5)
print('Вывод')
print(a)

print('Четные не четные')
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_noteven_numbers(test_list, 'четные'))

print('Декоратор')

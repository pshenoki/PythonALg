""" Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]. """

from collections import deque

a = list(input('Введите первое число: '))
b = list(input('Введите второе число: '))


def sum_(x, y):
    N = 16  # размерность
    my_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    my_reverse_dict = {}  # создадим обратный словарь
    for key, value in my_dict.items():
        my_reverse_dict[value] = key

    if len(x) > len(y):
        x, y = deque(x), deque(y)
    else:
        x, y = deque(y), deque(x)

    res_dec = deque()
    jump_one = 0
    for _ in range(len(x)):
        if y:
            result = my_dict[x.pop()] + my_dict[y.pop()] + jump_one
        else:
            result = my_dict[x.pop()] + jump_one

        jump_one = 0
        if result < N:
            res_dec.appendleft(my_reverse_dict[result])
        else:
            res_dec.appendleft(my_reverse_dict[result - N])
            jump_one = 1

    if jump_one == 1:
        res_dec.appendleft('1')
    return list(res_dec)


print(sum_(a, b))

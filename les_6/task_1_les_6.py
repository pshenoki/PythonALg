"""Определить, какое число в массиве встречается чаще всего."""
import random as r
from collections import Counter
import sys

""" Python 3.8.3 [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32 """

SIZE = 2000
MIN_ITEM = 1
MAX_ITEM = 1000
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

my_list = []                # как я понял, питон уже выделил память для этих чисел
for i in range(-5, 257):
    my_list.append(id(i))
CONSTANT_MEM = 6384


def list_memory(obj):
    if id(obj) in my_list:
        return False
    my_list.append(obj)
    return True


def one_obj_mem(obj):
    sum_ = 0
    if list_memory(obj):
        sum_ += sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key_, value in obj.items():
                if list_memory(key_):
                    sum_ += sys.getsizeof(key_)
                if list_memory(value):
                    sum_ += sys.getsizeof(value)
        elif not isinstance(obj, str):
            for item in obj:
                if list_memory(item):
                    sum_ += sys.getsizeof(item)
    return sum_


def sum_list_mem(m_list):
    sum_ = 0
    for obj in m_list:
        sum_ += one_obj_mem(obj)
    return f"{sum_} + {CONSTANT_MEM} = {sum_ + CONSTANT_MEM}"


# Вариант № 1

my_dict = {}
for i in array:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1

spam_key = array[0]
spam_val = my_dict[array[0]]

for key, val in my_dict.items():
    if val > spam_val:
        spam_key = key
        spam_val = val

print(f"Значение {spam_key} встречается {spam_val} раз")
final_list_1 = [SIZE, MIN_ITEM, MAX_ITEM, array, my_dict, key, val, i]
print(sum_list_mem(final_list_1))

""" в общей сложности программа заняла в памяти 120124 
    это достаточно неплохо, так  как мы не создвали ничего
    лишнего.
    Эта программа заняла меньше всего места"""


# Вариант № 2

my_list = []
for i in range(-5, 257):
    my_list.append(id(i))
CONSTANT_MEM = 6384

a = Counter(array)
my_tuple = a.most_common()[0]

print(f"Значение {my_tuple[0]} встречается {my_tuple[1]} раз")
final_list_2 = [SIZE, MIN_ITEM, MAX_ITEM, array, a, my_tuple]
print(sum_list_mem(final_list_2))

""" в общей сложности программа заняла в памяти 120168 
    это достаточно неплохо. Если учесть, что было написано всего 2 строчки кода,
    можно сделать вывод, что модуль коллекции просто офигителен!
    Эта программа заняла практически столько же места как и первая"""


# Вариант № 3 туповатый

my_list = []
for i in range(-5, 257):
    my_list.append(id(i))
CONSTANT_MEM = 6384


my_dict_3 = {}
sort_arr = sorted(array)  # добавил, чтобы посмотреть сколько жрет один лишний список)
for i in sort_arr:
    my_dict_3[i] = sort_arr.count(i)

a = max(my_dict_3.values())
for key, val in my_dict_3.items():
    if val == a:
        key = key
        break

print(f"Значение {key} встречается {val} раз")
final_list_3 = [SIZE, MIN_ITEM, MAX_ITEM, array, my_dict_3, a, sort_arr, key, val]
print(sum_list_mem(final_list_3))

""" в общей сложности программа заняла в памяти 173844 
    Это достаточно много, по сравнению с другими вариантами!
    На это повлияло создание дополнительного списка.
    Эта программа заняла больше всего места"""

""" Значения могут отличаться, так как массив создается случайно"""

""" Общий вывод: варианты 1 и 2 показали примерно одинаковый результат в отличии от варианта № 3
    по количеству занимаемой памяти.
    Если учесть затратность по времени написания, я бы выбрал вариант №2 :) """

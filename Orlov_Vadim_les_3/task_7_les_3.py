"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться. """

import random as r

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 11
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_value_1, min_value_2 = MAX_ITEM, MAX_ITEM + 1
for i in array:
    if i <= min_value_1:
        min_value_2, min_value_1 = min_value_1, i
    elif min_value_1 < i < min_value_2:
        min_value_2 = i
print(f" минимальные значения: {min_value_1}, {min_value_2}")

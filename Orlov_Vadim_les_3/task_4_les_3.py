"""Определить, какое число в массиве встречается чаще всего."""
import random as r

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 3
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_dict = {}
for i in array:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)

spam_key = array[0]
spam_val = my_dict[array[0]]

for key, val in my_dict.items():
    if val > spam_val:
        spam_key = key
        spam_val = val
print(f"Значение {spam_key} встречается {spam_val} раз")

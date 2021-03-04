"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать"""
import random as r

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    spam_max, spam_min = array[0], array[1]
    max_ind, min_ind = 0, 1                 # пришлось написать из-за: Name 'min_ind', 'max_ind'  can be undefined
else:
    spam_max, spam_min = array[1], array[0]
    max_ind, min_ind = 1, 0                 # пришлось написать из-за: Name 'min_ind', 'max_ind'  can be undefined

for num, i in enumerate(array):
    if i > spam_max:
        spam_max = i
        max_ind = num
    if i < spam_min:
        spam_min = i
        min_ind = num

if min_ind < max_ind:
    left_bord, right_bord = min_ind, max_ind
else:
    left_bord, right_bord = max_ind, min_ind

sum_ = 0
for i in range(left_bord + 1, right_bord):
    sum_ += array[i]
print(f"интервал : {left_bord} - {right_bord}")
print(f"сумма элементов : {sum_}")

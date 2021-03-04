"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """
import random as r

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [r.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    spam_max, spam_min = array[0], array[1]
    max_ind, min_ind = 0, 1                 # пришлось написать из-за: Name 'min_ind', 'max_ind'  can be undefined
else:
    spam_max, spam_min = array[1], array[0]
    max_ind, min_ind = 1, 0                 # пришлось написать из-за: Name 'min_ind', 'max_ind'  can be undefined

""" for i in array:
    if i > spam_max:
        spam_max = i
    if i < spam_min:                         # первый вариант
        spam_min = i
max_ind = array.index(spam_max)
min_ind = array.index(spam_min) """

for num, i in enumerate(array):
    if i > spam_max:
        spam_max = i                          # но этот, наверно, лучше
        max_ind = num                         # хотя не уверен :)
    if i < spam_min:
        spam_min = i
        min_ind = num

array[max_ind], array[min_ind] = array[min_ind], array[max_ind]

print(f"{spam_max:<2} - max elem")
print(f"{spam_min:<2} - min elem")
print(array)

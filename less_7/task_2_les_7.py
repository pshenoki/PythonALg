"""массив разбивается пополам, и каждая из половин делиться до тех пор,
пока размер очередного подмассива не станет равным единице;

далее выполняется операция алгоритма, называемая слиянием.
Два единичных массива сливаются в общий результирующий массив,
при этом из каждого выбирается меньший элемент (сортировка по возрастанию)
и записывается в свободную левую ячейку результирующего массива.
После чего из двух результирующих массивов собирается третий общий отсортированный массив, и так далее.
В случае если один из массивов закончиться, элементы другого дописываются в собираемый массив;

в конце операции слияния, элементы перезаписываются из результирующего массива в исходный."""
from math import inf
import random
SIZE = 10
LEFT_B = 0
RIGHT_B = 50 - 1 / inf
a = [round(random.uniform(LEFT_B, RIGHT_B), 3) for _ in range(SIZE)]  # прошу прощения за интервал,это все,что придумал)
print(f"{a} - начальный массив")


def merge_sort(arr1, arr2):
    x, y = 0, 0
    new_arr = []

    b_arr, s_arr = arr1, arr2
    if arr1[-1] < arr2[-1]:
        b_arr, s_arr = arr2, arr1

    while x < len(b_arr) and y < len(s_arr):
        if b_arr[x] < s_arr[y]:
            new_arr.append(b_arr[x])
            x += 1
        else:
            new_arr.append(s_arr[y])
            y += 1

    for tail in range(x, len(b_arr)):
        new_arr.append(b_arr[tail])

    return new_arr


def split_arr_and_sort(arr):
    if len(arr) == 1:
        return arr
    half = len(arr) // 2
    left = split_arr_and_sort(arr[:half])
    right = split_arr_and_sort(arr[half:])
    return merge_sort(left, right)


print(f"{split_arr_and_sort(a)} - отсортированный массив")

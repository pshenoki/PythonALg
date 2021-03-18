import random
SIZE = 10
array = [random.randint(-100, 99) for _ in range(SIZE)]
print(f"{array} - начальный массив")


def bubble_sort(arr):
    n = 1
    not_sorted = True

    while n < len(arr) and not_sorted:
        not_sorted = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                not_sorted = True

        if not_sorted:
            n += 1
            print(f"{arr} - проход № {n - 1} ")

    return arr


print(f"{bubble_sort(array)} - отсортированный массив")

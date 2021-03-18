import random
LEFT_B = 5
RIGHT_B = 20
size = random.choice([i for i in range(random.randint(LEFT_B, RIGHT_B)) if i % 2 == 1])
array = [random.randint(0, 10) for _ in range(size)]
print(f"{array} - начальный массив")


def gnome(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


my_arr = gnome(array)
print(f"{my_arr} - отсортированный массив")

print(f"{my_arr[len(array) // 2]} - медиана")

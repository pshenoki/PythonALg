"""В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9"""


LEFT_BOARD_i = 2
RIGHT_BOARD_i = 99
LEFT_BOARD_j = 2
RIGHT_BOARD_j = 9

for j in range(LEFT_BOARD_j, RIGHT_BOARD_j + 1):
    count = 0
    for i in range(LEFT_BOARD_i, RIGHT_BOARD_i + 1):
        if i % j == 0:
            count += 1
    print(f" В диапазоне натуральных чисел от {LEFT_BOARD_i} до {RIGHT_BOARD_i} \n "
          f"{count} чисел кратных {j}")

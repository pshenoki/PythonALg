"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

letter1 = int(input('Введите цифру в интервале от 1 до 26 включительно: '))

position1 = chr(letter1 + 96)

if 1 <= letter1 <= 26:
    print(f"{letter1} - позиция буквы '{position1}'")
else:
    print(f"Число не находится в заданном интервале")

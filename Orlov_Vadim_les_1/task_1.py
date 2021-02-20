""" ссылка на диаграммы https://drive.google.com/file/d/1xtzb8vTqTQYw4fqv5iujAJfXMtDvVvbK/view?usp=sharing """

"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь """

a = int(input('Введите трехзначное число: '))

x1 = a // 100
x2 = (a - (x1 * 100)) // 10
x3 = a % 10

print(f" Произведение цифр числа {a}: {x1 * x2 * x3}")
print(f" Сумма цифр числа {a}: {x1 + x2 + x3}")

""" ссылка на диаграммы https://drive.google.com/file/d/1s03hmoQ65rfoI07TfqhZ8J0XCMbTr9Hx/view?usp=sharing"""

"""Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5) """

number = input('Введите натуральное число: ')

even_count = 0
odd_count = 0

for i in number:
    if int(i) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f" для числа {number}:\n "
      f"{even_count} - четных цифр \n "
      f"{odd_count} - нечетных цифр ")

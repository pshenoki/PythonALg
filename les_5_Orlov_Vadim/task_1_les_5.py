""" Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""
from collections import defaultdict

QUARTER = 4
my_comp = defaultdict(list)
mean_profit = 0
num = int(input("Введите количество предприятий: "))

for _ in range(num):
    name = input("Введите уникальное название предприятия: ")
    for num_of_quarter in range(1, QUARTER + 1):
        profit = int(input(f"Введите прибыль за {num_of_quarter}-й квартал: "))
        my_comp[name].append(profit)

    mean_of_comp = sum(my_comp[name]) / QUARTER
    my_comp[name].append(mean_of_comp)
    mean_profit += mean_of_comp

for company, profit in my_comp.items():
    if profit[-1] > mean_profit / num:
        print(f"{company:<8} - {profit[-1]} - выше средней")

print(f'  {round(mean_profit / num, 2):>13} - средняя прибыль')

for company, profit in my_comp.items():
    if profit[-1] <= mean_profit / num:
        print(f"{company:<8} - {profit[-1]} - ниже средней")
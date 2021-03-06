"""Алгоритм нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Без помощи алгоритма «Решето Эратосфена» """
import timeit
import cProfile
import matplotlib.pyplot as plt


def analysis(func):
    left_b = 10
    right_b = 1000
    step_ = 50
    x_interval = [i for i in range(left_b, right_b, step_)]

    y_point = []
    for step in x_interval:
        y_point.append(timeit.timeit(f'{func.__name__}({step})', number=10, globals=globals()))

    cProfile.run(f'{func.__name__}(900)')

    plt.title(f'{func.__name__}')
    plt.plot(x_interval, y_point)
    plt.show()

    print(f" Наша функия - {func.__name__}")


def prime(n):
    simple_list = [2, 3]
    start = 4
    while len(simple_list) < n:
        count = 0
        for i in range(2, start-1):
            if start % i == 0:
                count += 1
                break
        if count == 0:
            simple_list.append(start)
        start += 1
    return simple_list[-1]


analysis(prime)

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.188    0.188 <string>:1(<module>)
#        1    0.187    0.187    0.188    0.188 task_2.2_les_4.py:29(prime)
#        1    0.000    0.000    0.188    0.188 {built-in method builtins.exec}
#     6995    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      898    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

""" Похоже на квадратичную зависимость O(n**2)"""

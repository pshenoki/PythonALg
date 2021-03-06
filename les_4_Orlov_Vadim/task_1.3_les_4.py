""" Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры """
import timeit
import cProfile
import matplotlib.pyplot as plt


def analysis(func):
    left_b = 0
    right_b = 500
    step_ = 50
    x_interval = [i for i in range(left_b, right_b, step_)]

    y_point = []
    for step in x_interval:
        y_point.append(timeit.timeit(f'{func.__name__}({step})', number=1000, globals=globals()))

    cProfile.run(f'{func.__name__}(900)')

    plt.title(f'{func.__name__}')
    plt.plot(x_interval, y_point)
    plt.show()

    print(f" Наша функия - {func.__name__}")


def stupid_func(n):
    my_list = []
    for i in range(n):
        my_list.append(1/(-2)**i)
    sum_ = 0
    for i in my_list:
        for j in my_list:
            if i == j:
                sum_ += i
    return sum_


analysis(stupid_func)

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.026    0.026 <string>:1(<module>)
#        1    0.026    0.026    0.026    0.026 task_1.3_les_4.py:28(stupid_func)
#        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
#      900    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

""" Похоже на квадратичную зависимоть  О(n**2)"""
""" Вывод : Самая долгая функция """

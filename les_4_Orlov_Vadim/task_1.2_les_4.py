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


def geom_pro(n):
    b1 = 1
    q = -1 / 2
    s = b1*(q**n - 1)/(q-1)
    return s


analysis(geom_pro)


#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_4_les_2.py:27(geom_pro)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

""" Похоже на константную зависимоть  О(1)"""
""" Вывод : Самая быстрая функция """

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


def recursion(n, sums=0, start=1):
    if n == 0:
        return sums
    sums += start
    start /= (-2)
    return recursion(n-1, sums, start)


analysis(recursion)

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    901/1    0.001    0.000    0.001    0.001 task_4_les_2.py:9(recur)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

''' Похоже на линейную зависимость О(n) '''
''' Вывод : Не так уж и плохо '''

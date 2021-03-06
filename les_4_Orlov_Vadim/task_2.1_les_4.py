"""Алгоритм нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
С помощью алгоритма «Решето Эратосфена» """
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


def sieve(n):
    k = 10  # Коэфициент моей асимптоты (я не могу точно сказать, как он работает, но чем больше n, тем нужно больше k
    # просто, если взять k = n**2, то работать будет всегда, но не так быстро и зависимость будет O(n**2)
    a = [0] * (n*k)  # создание массива с n количеством элементов
    for i in range((n*k)):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < (n*k):  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < (n*k):
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
         b.append(a[i])
    del a
    return b[n-1]


analysis(sieve)

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#        1    0.008    0.008    0.008    0.008 task_2.1_les_4.py:29(sieve)
#        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#     1600    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

""" Похоже на линейную зависимость O(n**2)"""

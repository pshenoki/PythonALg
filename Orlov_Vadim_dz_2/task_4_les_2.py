""" Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры """

numb = int(input('Введите количество элементов последовательности: '))


def sequence(n, sums=0, start=1):
    if n == 0:
        return sums
    sums += start
    start /= (-2)
    return sequence(n-1, sums, start)


print(sequence(numb))

""" Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке. """

BORD_UP = 127
BORD_DOWN = 32
GROUP_BY = 10

for i in range(BORD_DOWN, BORD_UP + 1):
    print(f"     {chr(i)} - {i}", end=";\n " if (i+1) % GROUP_BY == BORD_DOWN % GROUP_BY else "; ")

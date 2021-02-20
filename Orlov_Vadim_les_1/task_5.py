""" Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв """

letter1 = (input('Введите первую букву: '))
letter2 = (input('Введите вторую букву, буква должна отличтаться от первой: '))

position1 = ord(letter1) - 96
position2 = ord(letter2) - 96

if position1 > position2:
    letters_between = position1 - position2 - 1
else:
    letters_between = position2 - position1 - 1

print(f"{position1} - позиция буквы '{letter1}'")
print(f"{position2} - позиция буквы '{letter2}'")
print(f"{letters_between} - букв между ними")

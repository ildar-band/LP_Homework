'''
Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.
'''

def compare_strings(s1, s2):
    if (s1 == s2):
        result = 1
    elif (len(s1) > len(s2)):
        result = 2
    elif (s2 == 'learn'):
        result = 3
    else:
        result = ''
    return result

s1 = input('Введите первое слово: ')
s2 = input('Введите второе слово: ')

print('Результат: ' + str(compare_strings(s1, s2)))
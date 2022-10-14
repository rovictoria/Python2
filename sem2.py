# 1. Дано число N. Найти все его делители. Для
# каждого делителя укажите чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный),
# # 1(нечётный)
from pickletools import string1


print('1. Поиск делителей числа, их проверка на чётность/нечётность')
def CheckEven(x):  #функция возвращает саму строку, так, помимо вызова нужно добавить печать
    if x % 2 == 0:
        return '- чётный'
    else:
        return '- нечётный'

#процедуру же могу просто вызвать, без return, а в ней прописать вывод через print (печать)
def Example1():
    number = 60
    for i in range(1, number+1):
        if number % i == 0:
            print(i, end=' ')
            print(CheckEven(i))


Example1()

# Задача 2
print('2. Таблица истинности для (не Х или Y)')
def Example2():
    print(f'x | y | ¬ x ∨ y |')
    for x in range(0,2):
        for y in range (0,2):
            print(f'{x} | {y} |    {int(not x or y)}    |')

Example2()

# 3. Программа, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в
# другую. «qwe» «qwertyqwe» -> 2 раза (срезами по строке прохожу)
print(f'3. Количество вхождений меньшей строки в большую')

string1 = input('Введите 1 строку: ')
string2 = input('Введите 2 строку: ')
count = 0
if len(string1) > len(string2):
    max = string1
    min = string2
else: 
    max = string2
    min = string1
for i in range(len(max)):
        if min == max[i:i+len(min)]:
            count += 1
print(f'Количество вхождений "{min}" в "{max}" = {count}')
print(f'Или решение методом count: "{min}" в "{max}" = {max.count(min)}')

# 4. Дано число N. Заполнить список длиной N элементами
# 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]

# 5. Найдите все числа до 10000, у который
# количество делителей равно 10. 
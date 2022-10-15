import math
import re

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11
print('Дополнительно: сумма цифр вещественного числа.') 
def Sum_of_numbers():
    number = float(input('Введите число: '))
    number = abs(number)
    i = 0

    if number % 1 == 0:
        while abs(number) > 0:
            i += number % 10
            number = int(number / 10)
    else: 
        while number > 0:
            i += int(number*10)
            number = number*10 - int(number*10)
    print(i)
Sum_of_numbers()

# 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('1. Заполнение списка длиной N факториалами')
def Factorial(): 
    N = int(input('Введите N, до которого (включительно) нужно вывести факториалы: '))
    list = []
    number = 1
    for i in range(1, N+1): #будет от 0 до N-1 индексы (то есть 5 элементов выведет, а не до 5 степени включительно)
        number *= i
        list.append(number)
    print(list)
Factorial()

# 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print('2. Таблица истинности для (не (Х и Y) или Z)')
def True_false():
    print(f'x | y | z | ¬(x ∧ y) ∨ z |')
    for x in range(0,2):
        for y in range (0,2):
            for z in range (0,2):
                print(f'{x} | {y} | {z} |       {int(not (x and y) or z)}      |')

True_false()

# 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
print(f'3. Количество вхождений меньшей строки в большую')
def Elements_counter():
    string1 = input('Введите 1 строку: ')
    string2 = input('Введите 2 строку: ')
    for i in range(len(string1)):
        results = len(re.findall(string1[i], string2))
        print(f'{string1[i]} входит в {string2} - {results} раз(-а)')

Elements_counter()

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
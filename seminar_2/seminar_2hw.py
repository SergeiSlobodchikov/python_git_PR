# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# numbers = str(input('Введите число чтобы узнать сумму его цифр: '))
# summa = 0

# for char in numbers:
#     if char.isdigit():
#         summa += int(char)

# print(summa)

# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите натуральное число '))
# numbers = 1
# while n <= 0:
#     n = int(input('Введите натуральное число '))
# if n == 0:
#     print('Вы ввели 0')
# else:
#     for i in range(n):
#         i = i + 1
#         numbers = i * numbers
#         print(f'{numbers}', end=' ')
# print()


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите количество чисел в списке '))
# lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'Список {lst}, сумма чисел из списка {round(sum(lst), 2)}')


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# number = int(input('Задайте число N для создания списка: '))
# if number >= 0: 
#     num = number*(-1)
# else:
#     num = number
#     number = number*(-1)
# spisok = []
# while number >= num:
#     spisok.append(num)
#     num += 1

# print(spisok)

# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
file = open('/Users/david/Desktop/python/homework/lesson2/task17.txt')
positions = []
for i in file.read():
    if i.isdigit():
        positions.append(int(i))


# Реализуйте алгоритм перемешивания списка.

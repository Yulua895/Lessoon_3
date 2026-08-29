# Условие задачи:

from random import choice
from unittest import result




# Доработайте программу калькулятора calc_dz.py. Добавьте функцию, которая позволит пользователю просматривать историю
# всех выполненных ранее вычислений. Это функция будет читать данные из файла, в который записываются результаты
# (calculations.txt), и выводить их пользователю.

# Выберите операцию:
# 1. Сложение
# 2. Вычитание
# 3. Умножение
# 4. Деление
# 5. Просмотр историй вычеслений
# Введите номер операции (1/2/3/4/5) : 5
# История вычеслений:
# Результат: 1 + 1 = 2
# Результат: 2 - 2 = 0
# Результат: 3 * 3 = 9
# Результат: 4 / 4 = 1.00
# Результат: 1 + 1 = 2
# Результат: 44 + 77 = 121


# Решение:


# def add(h, i):
#     return h + i
#
#
# def subtract(h, i):
#     return h - i
#
#
# def multiply(h, i):
#     return h * i
#
#
# def divide(h, i):
#     if i == 0:
#         return 0
#     return h / i
#
#
# def calculations_history():
#     document = 'calculations.txt'
#     with open(document, 'r', encoding='utf-8') as file:
#             content = file.read()
#     return content
#
#
#
#
#
#
# print('Выберете операцию: ')
# print('1. Сложение')
# print('2. Вычитание')
# print('3. Умножение')
# print('4. Деление')
# print('5. Просмотр истории вычеслений')
#
# choice = int(input('Введите номер операции (1/2/3/4/5): '))
#
# if choice > 5:
#     print('Неверный ввод')
# elif choice == 5:
#     print(f'Просмотр истории вычеслений\n {calculations_history()}')
#
# else:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#
#     if choice == 1:
#         result = f'Результат: {num1} + {num2} = {add(num1, num2)}'
#     elif choice == 2:
#         result = f'Результат: {num1} - {num2} = {subtract(num1, num2)}'
#     elif choice == 3:
#         result = f'Результат: {num1} * {num2} = {multiply(num1, num2)}'
#     elif choice == 4:
#         result = f'Результат: {num1} / {num2} = {divide(num1, num2)}'
#     else:
#         print('Неверный ввод')
#
#     with open('calculations.txt', 'w+', encoding='utf-8') as file:
#         content = file.write(f'{result}\n')



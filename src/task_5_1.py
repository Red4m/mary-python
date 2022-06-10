"""Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0')"""
x = input('Enter x: ')
while x.isdigit() is False:
    x = input('Incorrect input. Enter an integer number: ')
x = int(x)
y = input('Enter y: ')
while y.isdigit() is False:
   y = input('Incorrect input. Enter an integer number: ')
y = int(y)
while (True):
    sign = input('Enter a sign for operation (might be "+", "-", "/" or "*"). Enter 0 for exit: ')
    while sign != '+' and sign != '-' and sign != '/' and sign != '*' and sign != '0':
        sign = input('Incorrect input. Enter the sign again: ')
    if sign == '+':
        z = x + y
    elif sign == '-':
        z = x - y
    elif sign == '/':
        z = x / y
    elif sign == '*':
        z = x * y
    print('Z =', round(z, 4))
    if sign == '0':
        break

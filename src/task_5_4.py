"""Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число"""
n = input('Enter a number: ')
while n.isdigit() is False:
    n = input('Incorrect input. Enter an integer number: ')
n = int(n)
s = 0
for i in range(1, n+1):
    s += 1/i
print('Sum:', round(s, 4))

"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""
def fact2 (n):
    fact = 1
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            fact *= i
    else:
        for i in range(2, n+1, 2):
            fact *= i
    print(n, '!! =', fact)

for j in range(5):
    number = input("Enter a number: ")
    while (True):
        if number.isdigit() is True:
            number = int(number)
            break
        number = input('Incorrect input. Enter an integer number: ')
    fact2(number)

"""Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
100: 2 4 5 10 20 25 50
101:
102: 2 3 6 17 34 51
103:
104: 2 4 8 13 26 52
105: 3 5 7 15 21 35"""
m = input('Enter m: ')
while m.isdigit() is False:
    m = input('Incorrect input. Enter an integer number: ')
m = int(m)
n = input('Enter n: ')
while n.isdigit() is False:
    n = input('Incorrect input. Enter an integer number: ')
n = int(n)
if m > n:
    m, n = n, m
for i in range(m, n+1):
    list_of_dividers = ''
    for j in range(2, i):
        if i % j == 0:
            list_of_dividers += str(j) + ' '
    print(i, ':', list_of_dividers)

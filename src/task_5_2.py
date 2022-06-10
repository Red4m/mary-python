"""Дано число. Найти сумму и произведение его цифр"""
x = input('Enter a number: ')
while x.isdigit() is False:
    x = input('Incorrect input. Enter an integer number: ')
length = len(x)
x = int(x)
sum, mult = 0, 1
for i in range(length-1, -1, -1):
    sum += x // 10**i
    mult *= x // 10**i
    x -= (x // 10**i)*10**i
print('Sum:', sum, '\nMultiplication:', mult)

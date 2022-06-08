"""Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2"""
from random import randint

length = input('Enter a length for our list: ')
while length.isdigit() is False:
    length = input('Incorrect input. Enter a length for our list: ')
length = int(length)
arr = []
for i in range(length):
    arr.append(randint(0, 10))
print('Our list:', arr)
new_arr = []
for i in arr:
    new_arr.append(i*(-2))
print('New list. Solving with for-cycle:', new_arr)
while len(new_arr) != length:
    new_arr.append(arr.pop() * (-2))
print('New list. Solving with while-cycle:', new_arr)

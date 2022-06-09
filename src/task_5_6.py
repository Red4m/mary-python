"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)"""
from random import randint

length = input('Enter a length for our list: ')
while length.isdigit() is False:
    length = input('Incorrect input. Enter a length for our list: ')
length = int(length)
arr = [randint(0, 20) for i in range(length)]
print(arr)
result = 0
counter = 0
for j in range(len(arr)-1):
    if arr[j + 1] > arr[j] and counter == 0:
        counter += 1
        result += 1
    elif arr[j + 1] > arr[j] and counter != 0:
        counter += 0
    elif arr[j + 1] <= arr[j]:
        counter = 0
print('Result of parts:', result)

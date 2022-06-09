"""В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы."""
from random import randint

arr = []
for i in range(19):
    arr.append(randint(0, 10))
print('Our list:', arr)
for i in range(19):
    if arr[i] % 2 == 0:
        arr[i] = max(arr)
print('Edited list:', arr)

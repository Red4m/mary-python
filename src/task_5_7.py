"""Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
элемент и поменять его местами с элементом главной диагонали"""
from random import randint

n = input('Enter a size of square matrix: ')
while (True):
    if n.isdigit() is True:
        n = int(n)
        if n % 2 == 1:
            break
    n = input('Incorrect input. Enter an odd number: ')
matrix = [[randint(-10, 10) for i in range(n)] for i in range(n)]
for k in matrix:
    print(k)
for i in range(n):
    max_position = matrix[i].index(max(matrix[i]))
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[i][max_position] = max(matrix[i]), matrix[i][j]
for k in matrix:
    print(k)

from random import randint

length = input('Enter a length for our list: ')
while length.isdigit() is False:
    length = input('Incorrect input. Enter a length for our list: ')
length = int(length)
arr = [randint(0, 10) for i in range(length)]
print('Our list:', arr)
counter = 0
for i in arr:
    if i % 2 == 0:
        counter += 1
print('There are', counter, 'even numbers in the list. Solving with for-cycle')
counter = 0
while len(arr) > 0:
    element = arr.pop()
    if element % 2 == 0:
        counter += 1
print('There are', counter, 'even numbers in the list. Solving with while-cycle')

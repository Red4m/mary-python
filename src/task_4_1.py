from random import randint

length = input('Enter a length for our list: ')
while length.isdigit() is False:
    length = input('Incorrect input. Enter a length for our list: ')
length = int(length)
#arr = [randint(0, 10) for i in range(length)]
arr = []
for i in range(length):
    arr.append(randint(0, 10))
print('Our list:', arr)
new_arr = []
for i in arr:
    new_arr.append(i*(-2))
print('New list. Solving with for-cycle:', new_arr)
while len(new_arr) != length:
    element = arr.pop()
    new_arr.append(element*(-2))
print('New list. Solving with while-cycle:', new_arr)

from random import randint

length = input('Enter a length for our list: ')
while length.isdigit() is False:
    length = input('Incorrect input. Enter a length for our list: ')
length = int(length)
arr = [randint(0, 10) for i in range(length)]
print('Our list:', arr)
new_arr = []
for i in range(length-1):
    new_arr.append(arr[i+1])
new_arr.append(arr[0])
print('New list. Solving with for-cycle:', new_arr)
new_arr = []
while len(new_arr) != length-1:
    element = arr.pop(1)
    new_arr.append(element)
new_arr.append(arr[0])
print('New list. Solving with while-cycle:', new_arr)

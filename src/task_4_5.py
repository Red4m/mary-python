first_element = input('Enter the first element for fibonacci list: ')
while first_element.isdigit() is False:
    first_element = input('Incorrect input. Enter a length for our list: ')
first_element = int(first_element)
arr = [first_element, first_element]
for i in range(13):
    arr.append(arr[i] + arr[i+1])
print('Our list. Solving with for-cycle:', arr)
while len(arr) != 15:
    arr.append(arr[arr.index(first_element)] + arr[arr.index(first_element)+1])
print('Our list. Solving with while-cycle:', arr)

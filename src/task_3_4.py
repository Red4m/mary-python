str = input('Enter a string: ')
length = len(str)
if length%2==1:
    print('A result string: ' + str[length//2])
    if str[length//2]==str[0]:
        print('An additional string: ' + str[1:length-1])

str = input('Enter a string: ')
if len(str)%2==1:
    print('A result string: ' + str[(len(str)//2)])
    if str[(len(str)//2)]==str[0]:
        print('An additional string: ' + str[1:(len(str))-1])

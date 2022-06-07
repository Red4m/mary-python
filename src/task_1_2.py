x = float(input('Enter the first real number: '))
y = float(input('Enter the second real number: '))
print(f'Result: {round((abs(x)-abs(y))/(1+abs(x*y)), 5)}')

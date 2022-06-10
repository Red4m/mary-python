"""В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы"""
my_str = input('Enter a string: ')
arr = my_str.split(' ')
arr.reverse()
my_str = ' '.join(arr)
print('Result:', my_str)

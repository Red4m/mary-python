my_dict = my_dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
matrix_for_dict = []
for key in my_dict.keys():
    new_key = key + str(len(key))
    matrix_for_dict.append([new_key, my_dict[key]])
my_dict = dict(matrix_for_dict)
print('Result (with for-cycle):', my_dict)
matrix_for_dict = []
while len(my_dict1) != 0:
    matrix_for_dict.insert(0, my_dict1.popitem())
    if len(matrix_for_dict[0]) % 2 == 0:
        new_key = matrix_for_dict[0][0] + str(len(matrix_for_dict[0][0]))
        matrix_for_dict[0] = [new_key, matrix_for_dict[0][1]]
my_dict1 = dict(matrix_for_dict)
print('Result (with while-cycle):', my_dict1)

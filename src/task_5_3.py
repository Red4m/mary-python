"""Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300"""
list_of_sums = {}
for number in range(200, 301):
    list_of_dividers = []
    sum_of_dividers = 0
    for divider in range(1, number):
        if number % divider == 0:
            list_of_dividers.append(divider)
    sum_of_dividers = sum(list_of_dividers)
    list_of_sums[number] = sum_of_dividers
    for sum_other in list_of_sums.values():
        if number == sum_other:
            for para in list_of_sums.items():
                if para[0] == list_of_sums[number] and para[1] == number and para[0] != para[1]:
                    print('Friendly numbers:', para[0], para[1])

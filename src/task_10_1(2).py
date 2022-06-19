"""Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+."""

import csv

fields = ['firstname', 'lastname', 'age']
new_list = ["1-12 years", "13-18 years", "19-25 years", "26-40 years", "40+ years"]
my_rows = [
    ['Mariya', 'Epikhova', 20],
    ['Alena', 'Alkhovik', 20],
    ['Anna', 'Kholodok', 17],
    ['Mariya', 'Ivanova', 13],
    ['Alesya', 'Epikhova', 44],
    ['Anastasiya', 'Shapliko', 15],
    ['Ivan', 'Ivanov', 10],
    ['Kate', 'Black', 12],
    ['Stas', 'Sosedov', 35],
    ['Jesus', 'Christ', 33]
]


def my_decorator(func):

    def wrapper(file_n, field, *args):
        count_1_12 = count_13_18 = count_19_25 = count_26_40 = count_41 = 0
        for j in args:
            if int(j[2]) <= 12:
                count_1_12 += 1
            elif int(j[2]) <= 18:
                count_13_18 += 1
            elif int(j[2]) <= 25:
                count_19_25 += 1
            elif int(j[2]) <= 40:
                count_26_40 += 1
            else:
                count_41 += 1
            func('people_age.csv', new_list, [count_1_12, count_13_18, count_19_25, count_26_40, count_41])
    return wrapper


@my_decorator
def my_func_write(file_n, field, *args):
    with open(file_n, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(field)
        csvwriter.writerows(args)


my_func_write('file_10_11.csv', fields, *my_rows)

"""Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+."""

import csv

fields = ['firstname', 'lastname', 'age']
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
filename, filename_age = 'file_10_1.csv', 'file_age.csv'
my_rows2 = []

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(fields)
    csvwriter.writerows(my_rows)

with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    fields = next(csvreader)
    for row in csvreader:
        my_rows2.append(row)

new_list = ["1-12 years", "13-18 years", "19-25 years", "26-40 years", "40+ years"]
with open(filename_age, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(new_list)
    count_1_12 = count_13_18 = count_19_25 = count_26_40 = count_41 = 0
    for j in my_rows2:
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
    csvwriter.writerow([count_1_12, count_13_18, count_19_25, count_26_40, count_41])

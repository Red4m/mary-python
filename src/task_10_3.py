"""Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату."""

import csv
from datetime import date

my_rows = [
    date(day=30, month=12, year=2020),
    date(day=9, month=9, year=2022),
    date(day=1, month=9, year=2020),
    date(day=15, month=2, year=2010),
    date(day=9, month=7, year=2022),
    date(day=10, month=8, year=2022)
]
my_rows2 = []
filename = 'file_10_3.csv'

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(my_rows)

with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        my_rows2.append(row)

for i in my_rows2:
    print('The earliest date is', min(i))

'''
Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду (скорость ветра и
градусы) для Минск за последние 7 дней.
'''

import csv
from datetime import date, datetime

fields = ['date', 'place', 'degrees', 'wind speed']
my_rows = [
    [date(year=2020, month=9, day=9), 'Minsk', 20, 4],
    [date(year=2022, month=6, day=15), 'Minsk', 25, 3],
    [date(year=2022, month=6, day=16), 'Minsk', -10, 4.5],
    [date(year=2022, month=6, day=9), 'Minsk', 20, 5],
    [date(year=2022, month=6, day=17), 'Osipovichi', 20, 4],
    [date(year=2022, month=5, day=12), 'Minsk', 22, 10],
    [date(year=2022, month=6, day=18), 'Minsk', 20, 4],
    [date(year=2022, month=6, day=19), 'Minsk', 30, 1]
]
my_rows2 = []
filename = 'file_10_2.csv'
check_date = datetime(year=2022, month=6, day=12)
sum_of_degrees = sum_of_speed = counter = 0

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(fields)
    csvwriter.writerows(my_rows)

with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    fields = next(csvreader)
    for row in csvreader:
        my_rows2.append(row)

for row in my_rows2:
    if row[1] == 'Minsk':
        if datetime.strptime(row[0], '%Y-%m-%d') > check_date:
            sum_of_degrees += float(row[2])
            sum_of_speed += float(row[3])
            counter += 1

print('Average degrees', sum_of_degrees/counter, '\nAverage wind speed', sum_of_speed/counter)

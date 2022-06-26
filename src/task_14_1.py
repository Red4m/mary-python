"""Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!"""

from datetime import datetime, timedelta
from time import sleep
import argparse
import os


def my_generator(my_t: timedelta, delt: timedelta) -> timedelta:
    for _ in range(my_t.seconds + 1):
        yield my_t
        my_t -= delt


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hs', '--hours', required=True)
parser.add_argument('-ms', '--minutes', required=True)
parser.add_argument('-ss', '--seconds', required=True)
args = parser.parse_args()
os.mkdir('src/log')
with open('src/log/log.txt', 'w') as file:
    file.write(f'{args.first_name} {args.last_name}\n')
    file.write(str(datetime.now()))

my_time = timedelta(hours=int(args.hours), minutes=int(args.minutes), seconds=int(args.seconds))
delta = timedelta(seconds=1)
for j in my_generator(my_time, delta):
    print(j)
    sleep(1)
print('ALARM!!!')

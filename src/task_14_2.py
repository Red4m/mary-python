"""Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""

from datetime import datetime, timedelta
from time import sleep
import argparse
import os


def my_generator(my_t: timedelta, delt: timedelta) -> timedelta:
    """
    Generate reverse counting time
    :param my_t: start time
    :param delt: a step between start time and next time
    :return: changed time
    """
    for _ in range(my_t.seconds + 1):
        yield my_t
        my_t -= delt


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-foc', '--focus', type=int, default=25, required=False)
parser.add_argument('-br', '--break-time', type=int, default=5, required=False)
parser.add_argument('-cl', '--cycles', type=int, default=4, required=False)
parser.add_argument('-tn', '--task-name', required=True)

args = parser.parse_args()
if os.path.isdir('src/log') is False:
    os.mkdir('src/log')
with open('src/log/log.txt', 'a') as file:
    file.write(f'{args.first_name} {args.last_name}\n')
    file.write(args.task_name + '\n')
    file.write(str(datetime.now()) + '\n')
print(args.task_name)
for _ in range(args.cycles):
    print(f'Start focusing {args.focus} minutes')
    focus = my_generator(timedelta(minutes=args.focus), timedelta(seconds=1))
    for j in focus:
        print(j)
        sleep(1)
    print(f'Time for {args.break_time} minutes rest')
    rest = my_generator(timedelta(minutes=args.break_time), timedelta(seconds=1))
    for h in rest:
        print(h)
        sleep(1)
print("Good job! You've done your task!")

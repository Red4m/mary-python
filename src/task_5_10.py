"""Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут"""
from datetime import time

quantity = input('Enter a quantity of trains: ')
while quantity.isdigit() is False:
    quantity = input('Incorrect input. Enter a length for our list: ')
quantity = int(quantity)
values = ["name", "departure country", "departure time", "arrival country", "arrival time"]
list_of_trains = []
limit = time(hour=7, minute=20)
for i in range(quantity):
    train = {}
    for x in values:
        if x == "departure time" or x == "arrival time":
            train[x] = time(hour=int(input('Enter hours: ')), minute=int(input('Enter minutes: ')))
        else:
            train[x] = input('Enter ' + str(x) + ': ')
    list_of_trains.append(train)
for train in list_of_trains:
    if (train["arrival time"].hour * 60 + train["arrival time"].minute) - (train["departure time"].hour * 60 + train["departure time"].minute) > (limit.hour * 60 + limit.minute):
        print('Way time is more than 7 hours 20 minutes', train)

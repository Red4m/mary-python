"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    """
    Class works with cars
    """
    def __init__(self, index: int, model: str, year_of_issue: int, speed=0):
        """
        Constructor initializes car-object properties
        :param index: int number
        :param model: full name of car
        :param year_of_issue: year of issue
        :param speed: value of speed (default 0)
        """
        self.__index = index
        self.__model = model
        self.__year_of_issue = year_of_issue
        self.__speed = speed

    def speed_up(self):
        """
        Increase the speed on 5 points
        """
        self.__speed = self.__speed + 5

    def speed_down(self):
        """
        Decrease the speed on 5 points
        """
        self.__speed = self.__speed - 5

    def stop(self):
        """
        Reduce speed to zero
        """
        self.__speed = 0

    def show_speed(self):
        """
        Print the value of speed
        """
        print('Speed is', self.__speed)

    def speed_reverse(self):
        """
        Change speed sign
        """
        self.__speed = -self.__speed

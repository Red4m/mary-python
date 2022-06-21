"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(не 12:65:83, а 13:06:23)"""


class MyTime:
    def __init__(self, *args):
        if len(args) == 0:
            self.__hours = 0
            self.__minutes = 0
            self.__seconds = 0
        elif len(args) == 3:
            self.__hours = args[0]
            self.__minutes = args[1]
            self.__seconds = args[2]
        elif type(args[0]) is str:
            arr = args[0].split('-')
            self.__hours = int(arr[0])
            self.__minutes = int(arr[1])
            self.__seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            copy_time = args[0]
            self.__hours = copy_time.__hours
            self.__minutes = copy_time.__minutes
            self.__seconds = copy_time.__seconds

    @property
    def time_in_seconds(self) -> int:
        """
        Turn whole time into seconds
        :return: int number of time in seconds
        """
        return self.__seconds + self.__minutes * 60 + self.__hours * 60 ** 2

    def show_time(self):
        """
        Print pretty and correct time display
        """
        seconds = self.time_in_seconds
        if seconds > 24 * 60 ** 2:
            seconds -= 24 * 60 ** 2
            hours = seconds // 60 ** 2
        else:
            hours = seconds // 60 ** 2
        seconds -= hours * 60 ** 2
        minutes = seconds // 60
        seconds -= minutes * 60

        def normalize_time(number: int) -> str:
            """
            Add a zero at the beginning of number if necessary
            :param number: any part of time (hours, minutes, seconds)
            :return: right number
            """
            number = str(number)
            if len(number) == 1:
                number = '0' + number
            return number

        print(f'{normalize_time(hours)}:{normalize_time(minutes)}:{normalize_time(seconds)}')

    def __eq__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds == other.time_in_seconds

    def __ne__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds != other.time_in_seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds < other.time_in_seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds > other.time_in_seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds <= other.time_in_seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds >= other.time_in_seconds

    def __add__(self, other: 'MyTime') -> 'MyTime':
        new_time = MyTime(0, 0, self.time_in_seconds + other.time_in_seconds)
        return new_time

    def __sub__(self, other: 'MyTime') -> 'MyTime':
        if self > other:
            new_time = MyTime(0, 0, self.time_in_seconds - other.time_in_seconds)
        else:
            new_time = MyTime(0, 0, other.time_in_seconds - self.time_in_seconds)
        return new_time

    def __mul__(self, number: int) -> 'MyTime':
        new_time = MyTime(0, 0, self.time_in_seconds * number)
        return new_time

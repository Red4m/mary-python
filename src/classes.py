"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)."""


class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def add(self) -> int or float:
        return self.num1 + self.num2

    @property
    def sub(self) -> int or float:
        return self.num1 - self.num2

    @property
    def mul(self) -> int or float:
        return self.num1 * self.num2

    @property
    def div(self) -> float:
        return self.num1 / self.num2

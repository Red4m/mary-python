"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""


class Calculator:
    @staticmethod
    def __add__(num1, num2: int):
        return num1 + num2

    @staticmethod
    def __sub__(num1, num2: int):
        return num1 - num2

    @staticmethod
    def __mul__(num1, num2: int):
        return num1 * num2

    @staticmethod
    def __div__(num1: int, num2) -> float:
        return num1 / num2


main_handler = {
    '+': Calculator.__add__,
    '-': Calculator.__sub__,
    '*': Calculator.__mul__,
    '/': Calculator.__div__
}

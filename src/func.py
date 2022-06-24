"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""
from abc import ABC


class Abstract(ABC):
    pass


class Calculator(Abstract):
    @staticmethod
    def add(num1, num2: int):
        return num1 + num2

    @staticmethod
    def sub(num1, num2: int):
        return num1 - num2

    @staticmethod
    def mul(num1, num2: int):
        return num1 * num2

    @staticmethod
    def div(num1: int, num2) -> float:
        return num1 / num2

"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка"""

from functools import wraps


def decorator(funk):
    """
    Performs a preliminary check of the function data
    :param funk: any function
    :return: inner-function
    """
    @wraps(funk)
    def inner(*args: int) -> funk:
        """
        Removes all even elements from the list
        :param *args: int numbers
        :return: function with list of odd numbers
        """
        new_list = []
        for i in args:
            if i % 2 == 1:
                new_list.append(i)
        return funk(*new_list)
    return inner


@decorator
def my_list(*args: int) -> None:
    """
    Print numbers
    :param *args: int numbers
    """
    print(*args)


my_list(0, 0, 1, 88, 11, 2, 2, 5, 6, 5, 77, 77, 8, 9, 8, 10)

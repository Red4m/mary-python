"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный"""

from functools import wraps


def decorator(funk):
    """
    Change a queue of arguments
    :param funk: any function
    :return: inner-function
    """
    @wraps(funk)
    def inner(*args: any) -> funk:
        """
        Change the queue of arguments
        :param *args: any arguments
        :return: function with new queue of arguments
        """
        new_list = list(args)[::-1]
        return funk(*new_list)
    return inner


@decorator
def my_list(*args: any) -> None:
    """
    Print all arguments
    :param *args: tuple of arguments with different types
    """
    print(*args)


my_list([0, 0, 1, 88], {'hsgd': 5, 'kjh': 'dvsvd'}, [11, 2, 2, 5, 6], [5, 77, 77, 8, 9, 8, 10], 55, 83, {1: 'sfjdggafs', 2: 'hgvh'})

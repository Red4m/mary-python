"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

d = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(d(abc=5, d=50, c=40))

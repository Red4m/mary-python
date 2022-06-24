from classes import Math
from exceptions import correct_number, correct_sign


def main():
    n1 = correct_number()
    while (True):
        sign = correct_sign()
        if sign == 'exit':
            break
        n2 = correct_number()
        main_handler = {
            '+': Math(n1, n2).add,
            '-': Math(n1, n2).sub,
            '*': Math(n1, n2).mul,
            '/': Math(n1, n2).div
        }
        print(n1, sign, n2, '= ', end='')
        n1 = main_handler[sign]
        print(n1, '\n-----Next cycle-----\n', n1)

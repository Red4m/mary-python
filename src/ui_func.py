from func import Calculator
from exceptions import correct_number, correct_sign


def main():
    n1 = correct_number()
    while (True):
        sign = correct_sign()
        if sign == 'exit':
            break
        n2 = correct_number()
        print(n1, sign, n2, '= ', end='')
        n1 = main_handler[sign](n1, n2)
        print(n1, '\n-----Next cycle-----\n', n1)


main_handler = {
    '+': Calculator.add,
    '-': Calculator.sub,
    '*': Calculator.mul,
    '/': Calculator.div
}

def correct_number() -> int:
    while(True):
        try:
            num = input('Enter number ')
            num = int(num)
            break
        except ValueError:
            print('Incorrect input, it should be int number. Try again.')
    return num


class MyException(Exception):
    def __init__(self, message='Incorrect input, it should be only the sign +, -, * or /.'):
        super().__init__(message)


def correct_sign() -> str:
    while(True):
        try:
            sign = input('Enter +, -, *, / or "exit" ')
            if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == 'exit':
                break
            else:
                raise MyException
        except MyException:
            print('Incorrect input. Try again.')
    return sign

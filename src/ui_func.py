from abc import ABC, abstractmethod
from func import main_handler
from exceptions import correct_number, correct_sign


class AbstractInterface(ABC):
    @abstractmethod
    def main(self):
        pass


class Interface(AbstractInterface):
    def main(self):
        n1 = correct_number()
        while (True):
            sign = correct_sign()
            if sign == 'exit':
                break
            n2 = correct_number()
            print(n1, sign, n2, '= ', end='')
            n1 = main_handler[sign](n1, n2)
            print(n1, '\n-----Next cycle-----\n', n1)

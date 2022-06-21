"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран
Примечание: в рамках задание создать два файла: classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


class Figure:
    def __init__(self, *args: int):
        self._x1 = args[0]._x
        self._y1 = args[0]._y


class Circle(Figure):
    def __init__(self, radius: int, *args: int):
        self._radius = radius
        super().__init__(*args)

    @property
    def __str__(self):
        print('Circle-object')

    @property
    def square(self):
        return 3.14 * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * 3.14 * self._radius


class Triangle(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self._x2 = args[1]._x
        self._y2 = args[1]._y
        self._x3 = args[2]._x
        self._y3 = args[2]._y

    @property
    def __str__(self):
        print('Triangle-object')

    @property
    def sides(self):
        a = ((self._x3 - self._x2) ** 2 + (self._y3 - self._y2) ** 2) ** 0.5
        c = ((self._x2 - self._x1) ** 2 + (self._y2 - self._y1) ** 2) ** 0.5
        b = ((self._x3 - self._x1) ** 2 + (self._y3 - self._y1) ** 2) ** 0.5
        return a, b, c

    @property
    def square(self):
        a, b, c = self.sides
        p = self.perimeter / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    @property
    def perimeter(self):
        a, b, c = self.sides
        return a + b + c


class Square(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self._x2 = args[1]._x
        self._y2 = args[1]._y

    @property
    def __str__(self):
        print('Square-object')

    @property
    def side(self):
        a = ((self._x2 - self._x1) ** 2 + (self._y2 - self._y1) ** 2) ** 0.5
        return a

    @property
    def square(self):
        a = self.side
        return a ** 2

    @property
    def perimeter(self):
        a = self.side
        return a * 4

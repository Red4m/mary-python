"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""


class Person:
    def __init__(self, firstname: str, lastname: str, year_of_birth: int):
        """
        Constructor initializes person-object properties
        """
        self.__firstname = firstname
        self.__lastname = lastname
        self.__year_of_birth = year_of_birth

    @property
    def firstname(self) -> str:
        """
        Getter for firstname attribute
        :return: firstname
        """
        return self.__firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @property
    def year_of_birth(self) -> int:
        return self.__year_of_birth

    @firstname.setter
    def firstname(self, firstname: str):
        """
        Setter for firstname attribute
        :param firstname: string with firstname
        """
        self.__firstname = firstname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth

    def show_person_info(self):
        print('Firstname', self.__firstname)
        print('Lastname', self.__lastname)
        print('Year of birth', self.__year_of_birth)

    def adult_or_child(self):
        answer = 'Adult' if self.__year_of_birth < 2004 else 'Child'
        print(answer)


class Student(Person):
    def __init__(self, firstname: str, lastname: str, year_of_birth: int, faculty: str, speciality: str):
        super().__init__(firstname, lastname, year_of_birth)
        self.__faculty = faculty
        self.__speciality = speciality

    @property
    def faculty(self) -> str:
        return self.__faculty

    @property
    def speciality(self) -> str:
        return self.__speciality

    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty

    @speciality.setter
    def speciality(self, speciality):
        self.__speciality = speciality

    def show_person_info(self):
        super().show_person_info()
        print('Faculty', self.__faculty)
        print('Speciality', self.__speciality)


class Bread:
    def __init__(self, name: str, nutritional_value: int, weight=350):
        self.__name = name
        self.__nutritional_value = nutritional_value
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @property
    def nutritional_value(self) -> int:
        return self.__nutritional_value

    @property
    def weight(self) -> int:
        return self.__weight

    @name.setter
    def name(self, name: str):
        self.__name = name

    @nutritional_value.setter
    def nutritional_value(self, nutritional_value: int):
        self.__nutritional_value = nutritional_value

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    def bite(self):
        if self.__weight < 35:
            self.__weight = 0
        else:
            self.__weight -= 35

    def show_bread_info(self):
        print('Name', self.__name)
        print('Nutritional value', self.__nutritional_value)
        print('Weight', self.__weight)

"""1. Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число
2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""
def inches_to_centimeters (inches):
    """
    This method convert inches to centimeters
    :param inches:
    :return: print of converting
    """
    return print(inches, 'inches is', inches * 2.54, 'centimeters')

def centimeters_to_inches (centimeters):
    """
    This method convert centimeters to inches
    :param centimeters:
    :return: print of converting
    """
    return print(centimeters, 'centimeters is', round((centimeters / 2.54), 4), 'inches')

def miles_to_kilometers (miles):
    """
    This method convert miles to kilometers
    :param miles:
    :return: print of converting
    """
    return print(miles, 'miles is', miles * 1.609, 'kilometers')

def kilometers_to_miles (kilometers):
    """
    This method convert kilometers to miles
    :param kilometers:
    :return: print of converting
    """
    return print(kilometers, 'kilometers is', round((kilometers / 1.609), 4), 'miles')

def pounds_to_kilograms (pounds):
    """
    This method convert pounds to kilometers
    :param pounds:
    :return: print of converting
    """
    return print(pounds, 'pounds is', round((pounds / 2.205), 4), 'kilograms')

def kilograms_to_pounds (kilograms):
    """
    This method convert kilograms to kilograms
    :param kilograms:
    :return: print of converting
    """
    return print(kilograms, 'kilograms is', kilograms * 2.205, 'pounds')

def ounces_to_grams (ounces):
    """
    This method convert ounces to grams
    :param ounces:
    :return: print of converting
    """
    return print(ounces, 'ounces is', ounces * 28.35, 'grams')

def grams_to_ounces (grams):
    """
    This method convert grams to ounces
    :param grams:
    :return: print of converting
    """
    return print(grams, 'grams is', round((grams / 28.35), 4), 'ounces')

def gallons_to_liters (gallons):
    """
    This method gallons miles to liters
    :param gallons:
    :return: print of converting
    """
    return print(gallons, 'gallons is', round((gallons / 3.785), 4), 'liters')

def liters_to_gallons (liters):
    """
    This method convert liters to gallons
    :param liters:
    :return: print of converting
    """
    return print(liters, 'liters is', liters * 3.785, 'gallons')

def pints_to_liters (pints):
    """
    This method convert pints to liters
    :param pints:
    :return: print of converting
    """
    return print(pints, 'pints is', round((pints / 2.113), 4), 'liters')

def liters_to_pints (liters):
    """
    This method convert liters to pints
    :param liters:
    :return: print of converting
    """
    return print(liters, 'liters is', liters * 2.113, 'pints')

def entering_value ():
    """
    This method do input and input validation of some value
    :return: value
    """
    value = input("Enter a value: ")
    while (True):
        if value.isdigit() is True:
            value = float(value)
            break
        value = input('Incorrect input. Enter a number in the range from 0 to 12: ')
    return value


while(True):
    operation = input("What units of measure do you want to convert?\n"
          "Choose a number of operation:\n"
          "1. inches to centimeters\n"
          "2. centimeters to inches\n"
          "3. miles to kilometers\n"
          "4. kilometers to miles\n"
          "5. pounds to kilograms\n"
          "6. kilograms to pounds\n"
          "7. ounces to grams\n"
          "8. grams to ounces\n"
          "9. gallons to liters\n"
          "10. liters to gallons\n"
          "11. pints to liters\n"
          "12. liters to pints\n"
          "0 - to exit\n\n")
    while (True):
        if operation.isdigit() is True:
            operation = int(operation)
            if 0 <= operation < 13:
                break
        operation = input('Incorrect input. Enter a number in the range from 0 to 12: ')
    if operation == 1:
        inches_to_centimeters(entering_value())
    elif operation == 2:
        centimeters_to_inches(entering_value())
    elif operation == 3:
        miles_to_kilometers(entering_value())
    elif operation == 4:
        kilometers_to_miles(entering_value())
    elif operation == 5:
        pounds_to_kilograms(entering_value())
    elif operation == 6:
        kilograms_to_pounds(entering_value())
    elif operation == 7:
        ounces_to_grams(entering_value())
    elif operation == 8:
        grams_to_ounces(entering_value())
    elif operation == 9:
        gallons_to_liters(entering_value())
    elif operation == 10:
        liters_to_gallons(entering_value())
    elif operation == 11:
        pints_to_liters(entering_value())
    elif operation == 12:
        liters_to_pints(entering_value())
    else:
        break

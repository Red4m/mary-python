"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""

def palindrome(s):
    strings = s.split()
    for i in strings:
        new_word = i[::-1]
        if i == new_word:
            print(i, 'palindrome')


my_str = input('Enter a sentence: ')
palindrome(my_str)

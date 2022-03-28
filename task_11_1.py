# 1. Реализовать класс «Дата».
# Техническое задание:
#
# Конструктор принимает дату (параметр) в виде строки формата «день-месяц-год».
# Методы объекта:
# Первый с декоратором @classmethod. Извлекает число, месяц, год из строки «день-месяц-год», преобразовывает их к типу int. Возвращает три числа.
# Второй с декоратором @staticmethod. Проводит валидацию этих трех чисел, например, месяц — от 1 до 12, дней в месяце не более 31 - далее на ваш выбор. Вы можете использовать пакет datetime для проверки корректности даты. Подумайте что логично возвращать валидатору, какое значимое имя вы дадите этому методу?
# При создании объекта в конструкторе использовать оба указанных метода.
# Конструктор создает объект только если прошла валидация вторым методом.
# Объект «дата» хранится в виде трех чисел отдельно или в контейнере. В случае невозможности создать объект контруктор выкидывает исключение DateInitError c внятным диагностическим сообщением.
# Переопределить метод __str__ для печати числа в виде 2021.12.31
# Создать несколько экземпляров и распечатать их. Проверить работу на не валидных данных.
# Исключение от конструктора ловить в основном коде программы и подменять выводом диагностического сообщения (любого).
from datetime import date
import re

class DateInitError(ValueError):
    def __init__(self, txt):
        self.txt = txt

class Date:
    def __init__(self, date_string):

        match_result = re.match(r'^\d\d-\d\d-\d{4}$', date_string)
        if match_result is None:
            raise Exception(f"{date_string} - incorrect date format, use dd-mm-yyyy format")
        self.date_string = date_string
        self.day, self.month, self.year = map(int, date_string.split('-'))

    @classmethod
    def type(cls, date_string):
        try:
            day, month, year = [int(i) for i in date_string.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        # except DateInitError as e:
        except ValueError as e:
            return f"{e} Ошибка в указании даты! Используйте числовой формат ДД-ММ-ГГГГ."
    @staticmethod
    def is_valid_date(date_string):
        try:
            day, month, year = date_string.split('-')
            date(int(year), int(month), int(day))
            return "дата корректна"
        except DateInitError as e:
            return f"где-то ошибка {e}"
        except ValueError:
            return f"указана неверная дата {date_string}"
print(Date.is_valid_date('35-02-2015'))
print(Date.type('31,-13-2022'))


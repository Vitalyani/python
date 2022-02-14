# 4. Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced, если вы решали задание 2. Создать скрипт, импортировать в него модуль utils и выполнить несколько вызовов функции currency_rates. Убедиться, что ничего лишнего не происходит.
# Техническое задание
#
# В модуле utils не должно быть ничего лишнего, только создание функций. Если вы считает нужным поместить туда дополнительную инфу, например тесты - используйте конструкцию main.
# Основной скрипт импортирует модуль или требуемые функции модуля, например currency_rates и currency_rates_advanced.
# После импорта выполните вызов функций, аналогичный заданию 1 (и 2), чтобы убедиться, что все импортировалось верно.

import utils
char_code = 'usD'
url = "http://www.cbr.ru/scripts/XML_daily.asp"
print(utils.currency_rates(url,char_code))
print(utils.currency_rates(url,'eur'))
print(utils.currency_rates(url,'abc'))

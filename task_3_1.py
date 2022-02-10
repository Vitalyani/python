# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского
# на русский язык. Если перевод сделать невозможно, вернуть объект None.
# Примеры/Тесты:
#
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Техническое задание
#
# Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.
# Обратите внимание на глобальные и локальные объекты и на «чистоту функции»


def num_translate (numeral):
    num_e = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
             'five': 'пять', 'six': 'шесть', 'seven': 'семь',
             'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if numeral in num_e:
        return num_e[numeral]
    else:
        return None

num_translate('one')
num_translate('eight')
num_translate("two")
num_translate("eleven")
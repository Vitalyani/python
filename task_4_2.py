# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …) и возвращающую курс этой валюты по отношению к рублю.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. В каком формате возвращен ответ?
# Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной). Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.
# Примеры/Тесты:
#
#
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates(url, "USd")
# 71.7846
# >>> currency_rates(url, "EuR")
# 83.3347
# >>> currency_rates(url, "GBP")
# 98.3449
# >>> currency_rates(url, "GBP2")
# >>>
#
# Алгоритм
#
# Пример использования requests есть в методичке.
# Внимательно посмотрите все методы объекта str, которыми вы можете пользоваться. Обратите внимание, что у методов могу быть параметры, которые сильно облегчат вам работу.
# Помните, срез строки создает копию. Уверены ли вы, что вам нужна копия именно такого размера? Это увеличивает время выполнения и расходует память. Аналогично функция поиска требует времени для работы, можно ли оптимизировать поиск?
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Вспомните в каких случаях функция возвращает None.

from requests import get, utils
def currency_rates(url,char_code):

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    ct = response.content.decode(encoding=encodings)

    char_code = char_code.upper()
    if char_code in ct:
        fnd = ct.find(char_code)
        # Ничего лучше не придумал, чем искать в строке код валюты, от ее индекса искать срез строки
        # курса валюты (от '<Value>' + 7 символов (длина '<Value>') и до первого совпадения '</Value>').
        value = float((ct[(ct.find('<Value>', fnd) + 7):(ct.find('</Value>', fnd))]).replace(',', '.'))

        # Номинал конечно не нужен по условию задачи, но аналогично искал срез строки значения номинала:
        # nominal = int(ct[(ct.find('<Nominal>', fnd) + 9):(ct.find('</Nominal>', fnd))])

        return value
        # решил, что если нужен номинал, то нужен и сам код валюты
        # return value,nominal,char_code


# Коды валют: AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS,
# CNY, MDL, NOK, PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY

char_code = 'usD'
url = "http://www.cbr.ru/scripts/XML_daily.asp"

print(currency_rates(url,char_code))
print(currency_rates(url,'eur'))
print(currency_rates(url,'abc'))

# Здесь вывод значения с номиналом в виде: 76.5762 руб = 1 USD
# if currency_rates(url,char_code) == None:
#     print(currency_rates(url,char_code))
#     print('Такой код валюты отсутствует')
# else:
#     print(f'{currency_rates(url, char_code)[0]} руб = {currency_rates(url, char_code)[1]} {currency_rates(url, char_code)[2]}')

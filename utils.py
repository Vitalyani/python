# 4. Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced, если вы решали задание 2. Создать скрипт, импортировать в него модуль utils и выполнить несколько вызовов функции currency_rates. Убедиться, что ничего лишнего не происходит.

from requests import get, utils
def currency_rates(url,char_code):

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    ct = response.content.decode(encoding=encodings)

    char_code = char_code.upper()
    if char_code in ct:
        fnd = ct.find(char_code)
        value = float((ct[(ct.find('<Value>', fnd) + 7):(ct.find('</Value>', fnd))]).replace(',', '.'))
        return value

# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# Техническое задание:
#
# Лог файл: https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Функция парсинга строки лог-файла:
# Принимает аргумент - строку (по шаблону из лог-файла)
# возвращает кортеж из 6 элементов вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
# Вы можете не обращать внимание на IPv6 или явно учесть их в регулярном выражении, это будет очень хорошо.
# Проверьте работоспособность функции на нескольких строках лог файла.
# Распарсите весь файл и выведите на экран все IP, без повторений.
# Примеры/Тесты:
#
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

# Регулярка:
# (?P<remote_addr>(([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(\d{1,3}\.){3}\d{1,3})).+(?P<request_datetime>((\d{2})\/(\w{3})\/(\d{4})(\:\d{2}){3}(\s\+\d{4}))).+(?P<request_type>(GET|HEAD)).+(?P<requested_resource>(\/\w+\/\w+_\d)).+(?P<response_code>(\d{3})) (?P<response_size>(\d{1,}))

# так было бы короче наверное, если точно все IP правильные и начинаются сначала строки:
# (?P<remote_addr>(?:^.+))(?:\s-){2}\s\[(?P<request_datetime>[^\]]+)\].+(?P<request_type>(?:GET|HEAD))...
import re
def log_parse(line):
    RE_PARSE = re.compile(r"""
    (?P<remote_addr>(?:(?:[0-9A-Fa-f]{0,4}:){1,7}[0-9A-Fa-f]{0,4}|(?:\d{1,3}\.){3}\d{1,3}))    # IPv4/6 
    .+\[(?P<request_datetime>[^\]]+)\]    # дата(17/May/2015:08:05:49 +0000)
    .+(?P<request_type>(?:GET|HEAD))    #тип: GET или HEAD
    .+(?P<requested_resource>(?:\/\w+\/\w+_\d))    #/downloads/product_2
    .+(?P<response_code>(?:\d{3}))\s(?P<response_size>(?:\d{1,}))    # код и размер
    """, re.VERBOSE)
    # ничего умнее что бы избавиться от списка не придумал, кроме как взятия по индексу.
    tpl = RE_PARSE.findall(line)[0]
    return tpl

line = """
2607:f700:8001:134:68de:5e03:fb43:ef3f - - [02/Jun/2015:18:06:13 +0000] "GET /downloads/product_2 HTTP/1.1" 200 17394636 "-" "Wget/1.13.4 (linux-gnu)"
"""

line1 = """
91.194.188.90 - - [17/May/2015:10:05:51 +0000] "HEAD /downloads/product_2 HTTP/1.1" 200 0 "-" "Wget/1.13.4 (linux-gnu)"
"""
print('\nВывод двух строк, распарсенных из двух строк лога:\n')
print(log_parse(line))
print(log_parse(line1))
print('------------------\n')

set_ip = set()
with open('nginx_logs.txt', mode='r', encoding='utf-8') as f:
    for x in f:
        rez = log_parse(x)[0]
        set_ip.add(rez)
print('Вывод на экран всех IP распарсенного лог-файла, без повторений:')
print(set_ip)
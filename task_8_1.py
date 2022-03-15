# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Техническое задание:
#
# Функция:
# принимает один параметр - строку: email
# извлекает имя пользователя - то, что до @ и домен - то, что после @
# возвращает словарь вида {'username': <имя_пользователя>, 'domain': <домен>}
# Если адрес не валиден, выбросить исключение ValueError. Можно с сообщением вида «wrong email: <email_address>»
# Шаблон имени пользователя: латинские буквы, цифры и символы: '._+-
# Шаблон домена: латинские буквы, цифры и символы .-
# В домене обязательно должна быть хотя бы одна точка
# Не использовать методы строки для извлечения информации из email - только регулярные выражения
# email полностью парсится за «один проход». Используйте группы.
# Проверьте работоспособность функции на нескольких email. Обязательно на правильных и неправильных.
# Чтобы проверить работоспособность функции на разных данных, вам придется «ловить» исключение в основной программе и выводить сообщение.
# Примеры/Тесты:
#
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание:
#
# Подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении
# Имеет ли смысл в данном случае использовать функцию re.compile()?
# Не используйте слишком широкий шаблон для почты. Шаблон должен пропускать только то, что указано в условии
# Подумайте, сколько групп здесь используется?

import re

# Без использования функции re.compile():

def email_parse(email_address):
    RE_PARSE = (r"^(?P<username>[a-zA-Z0-9'._+-]+)@(?P<domine>[a-zA-Z0-9.-]+\.[\w]{2,})$")

    if re.search(RE_PARSE, email_address) == None:
        raise ValueError(f'неверный email: {email_address}')
    return re.search(RE_PARSE, email_address).groupdict()

# С использованием функции re.compile():

# def email_parse(email_address):
#     RE_PARSE = re.compile(r"^(?P<username>[a-zA-Z0-9'._+-]+)@(?P<domine>[a-zA-Z0-9.-]+\.[\w]{2,})$")
#
#     if RE_PARSE.search(email_address)== None:
#         raise ValueError(f'неверный email: {email_address}')
#     return RE_PARSE.search(email_address).groupdict()


# email = 'someone@geekbrains.ru'
print(email_parse('someone@geekbrains.ru'))
print(email_parse('Ani_v.v@geekbrains-re.ru'))
print(email_parse('someone@geekbrainsru'))
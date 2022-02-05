# 2. Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку
# Техническое задание:
#
# Список может содержать произвольное кол-во элементов. Его элементы - строки.
# Пример исходного списка: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Строки-элементы списка:
# могут содержать цифры, обозначающие часы/минуты/секунды: "1" "12" "55"; одна или две цифры, без привязки к ограничениям на 60 минут/секунд и 24 часа. Т.е. '79', 'минут' - это корректно.
# могут начинаться со знаков + или - и обозначают температуры: "+5", "-7"; любое целое число. В начале может быть знак плюс или минус, но может и не быть.
# могут быть просто символьными строками: слова
# в начале и конце строк-чисел пробелов нет.
# строки-числа и строки-слова не обязательно идут точно через один.
# Обработка списка:
# обособить каждое целое число кавычками (добавить строку-кавычку до и после элемента списка, являющегося числом)
# дополнить это число нулём до двух целочисленных разрядов
# Например исходный список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'].
# Тогда результирующий список: ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов'].
# Обработанный список вывести на экран
# Сформировать из обработанного списка строку, соединив все элементы
# Для примера выше: 'в "05" часов "17" минут температура воздуха была "+05" градусов'
# Вывести строку на экран.
# Обратите внимание на отсутствие "лишних" пробелов около кавычек, например '"08" минут' - правильно, а '" 08 " минут' - неправильно.
# Формат вывода результата:
# Исходный, результирующий список и строку выводим на экран через print.
#
# Примеры/Тесты:
# Исходный список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Новый список + добавление элементов-кавычек:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Исходный список:
# ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
# Новый список + добавление элементов-кавычек:
# ['примерно в', '"', '23', '"', 'часа', '"', '08', '"', 'минут', '"', '03', '"', 'секунд', 'температура', 'воздуха', 'была', '"', '-05', '"', 'градусов Цельсия', 'темп', 'воды', '"', '+12', '"', 'градусов', 'Цельсия']
#
# Примечание:
#
# Регулярные выражения не используем. Учимся парсить строку самостоятельно.
# Алгоритм
#
# Сколько проходов по списку вам понадобится? Достаточно одного прохода.
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком? Это первый шаг - парсить строку-число и добавлять нули по необходимости.
# Задание упрощенное
#
# Если у вас не получается добавить правильно элементы-кавычки - упростим задачу. Обработайте строки-числа в соответствии с условием задачи и вставьте кавычки прямо в эту же строку. Т.е. вы меняете элементы списка, не добавляя новых элементов.

# Приведена упрощенная задача.
some_list = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
new_list = []
for idx, x in enumerate(some_list):
    if x.count('+') or x.count('-'):
        x = f'\"{x.zfill(3)}"'
    if x.isnumeric():
        x = f'\"{int(x):02d}"'
    new_list.insert(idx, x)
print(some_list)
print((' ').join(new_list))

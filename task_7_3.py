# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# В папках mainapp, authapp и аналогичных могут быть и другие файлы, кроме приведенных в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым.
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

# 1.поиск в структуре папок templates
# 2.когда нашли папку templates ее и ее содержимое необходимо скопировать в корень
# 3.повторить, пока не найдутся все папки templates
import os
from shutil import copytree
# Директория, в которой будем искать папки 'templates':
root_dir = os.path.join('.','my_project1')
# Директория, 'templates' в которую будем записывать все, что найдем в папках
# 'templates' внутри 'my_project1'.
# Тут я не понял, где должна находиться папка
# 'templates', т.к. изображено одно, а написано другое. Поэтому оставлю оба варианта:
# path_new = os.path.join('.','my_project1','templates') # Внутри папки 'my_project1'
path_new = os.path.join('.','templates') # В корне, рядом с папкой 'my_project1'
dirname = 'templates'
# for root, dirs, files in os.walk(root_dir):
#     for d in dirs:
#         if d == dirname:
#             # print(os.path.join(root, d)) # печатать путь, где найдена папка 'templates'
#             copytree(os.path.join(root, d),path_new, dirs_exist_ok=True)


for root, dirs, files in os.walk(root_dir):
    for d in dirs:
        if d == dirname:
            # print(os.path.join(root, d)) # печатать путь, где найдена папка 'templates'
            try:
                copytree(os.path.join(root, d),path_new, dirs_exist_ok=True)
            except Exception as e:
                print(f'global error: {e}')
            else:
                print('директории успешно скопированы')
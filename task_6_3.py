# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в json-файл. Проверить сохранённые данные.
# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов. При формировании словаря хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.

from os.path import join
import json

# Читаем и преобразовывам файл с ФИО:
mpath = join('.','data_3','task_3_users.csv')
users = []
with open(mpath, 'r', encoding='utf-8-sig') as f_1:
    for line in f_1:
        users_1 = line.split(',')
        users.append(f'{users_1[0][0]}{users_1[1][0]}{users_1[2][0]}')
    # print(users)

# Читаем и преобразовывам файл с хобби:
hobby = []
with open(join('.','data_3','task_3_hobby.csv'), 'r', encoding='utf-8-sig') as f_2:
    for line in f_2:
        hobby_1 = line.replace(',',';').replace('\n','')
        hobby.append(hobby_1)
    # print(hobby)

# Формируем словарь из списка ФИО и списка хобби:
#
# Решил сначала создать словарь с ключами ФИО и пустыми значениями,
# а после объединить (update) с коротким словарем (по наименьшему из списков).
rez = dict.fromkeys(users)
rez.update(dict(zip(users,hobby)))
print(rez)

# Сохраняем словарь в json-файл:
# myfile = open(file='.\\data_3\\file.json',mode='wt',encoding='utf-8')
myfile = open(join('.','data_3','file.json'),mode='wt',encoding='utf-8')
str_json = json.dump(rez,myfile,indent=2, ensure_ascii=False)
myfile.close()

# Задание сделал без учета возможности совпадения ключей вида "ФИО",
# т.к. в задаче ничего не говорится про это, и что делать с хобби при совпадении "ФИО" тоже нет ни слова.




# Тут что-то пытался сделать без zip, но ничего не получилось
#rez = {users[i]: hobby[i] for i in range(len(users))}
# for el in rez:
#     print(el)

# length = len(hobby)
# for idx,x in enumerate(users):
#     if idx<length:
#         x,hobby[idx]
#     else:
#         x,None


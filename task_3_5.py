# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх заданных списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Техническое задание
#
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной длины.
# Проверьте работу функции для кол-ва шуток больше, чем длины списков слов и меньше.
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.
# Примеры/Тесты:
#
#
# >>> get_jokes(3, nouns, adverbs, adjectives)
# ['автомобиль ночью мягкий', 'лес сегодня утопичный', 'дом вчера зеленый']
# >>> get_jokes(5, nouns, adverbs, adjectives)
# ['автомобиль вчера зеленый',
#  'дом ночью мягкий',
#  'огонь ночью утопичный',
#  'дом позавчера зеленый',
#  'город вчера утопичный']
# >>>


from random import choice

def get_jokes(n, nouns, adverbs, adjectives):
    """returning n jokes formed from three random words taken from three given lists: snouns, adverbs, adjectives"""
    jokes = []
    for i in range(n):
        random_nouns = choice(nouns)
        random_adverbs = choice(adverbs)
        random_adjectives = choice(adjectives)
        str_jokes = f'{random_nouns} {random_adverbs} {random_adjectives}'
        jokes.append(str_jokes)
    return (jokes)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = 2
print(get_jokes(3,nouns,adverbs,adjectives))
print(get_jokes(n,nouns,adverbs,adjectives))
print(get_jokes(5,nouns,adverbs,adjectives=["вялый", "грустный", "бледный", "злой", "тяжелый"]))
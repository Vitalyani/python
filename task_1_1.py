# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры/Тесты:
#
# duration = 53: 53 сек
# duration = 153: 2 мин 33 сек
# duration = 4153: 1 час 9 мин 13 сек
# duration = 400153: 4 дн 15 час 9 мин 13 сек

# начал в 15 - закончил в 20, в общей сложности потратил 2,5 часа

duration = 400153
second_in_a_minute = duration % 60
minute = duration // 60
minute_in_a_hour = minute % 60
hour = minute // 60
hour_in_a_day = hour % 24
day = hour // 24
if minute < 1:
    print(duration, 'сек')
elif hour < 1:
    print(minute, 'мин', second_in_a_minute, 'сек')
elif day < 1:
    print (hour, 'час', minute_in_a_hour, 'мин', second_in_a_minute, 'сек')
else:
    print(day, 'дн', hour_in_a_day, 'час', minute_in_a_hour, 'мин', second_in_a_minute, 'сек')
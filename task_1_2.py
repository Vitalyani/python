# 2. Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# Техническое задание:
# 1. Для всех нечетных чисел диапазона [1, 1000]
# 2. При решении задачи использовать только арифмитическое операции и циклы.
# 3. Не используем списки, функцию range, преобразование в строку/список.
# Формат вывода результата:
# Вывод на экран формить в виде: xxxxxxx ^3: xxx; sum: xxx [сумма цифр]
# Например:
# 19 ^3: 6859 sum: 19 [ 28 ]
# 31 ^3: 29791 sum: 50 [ 28 ]
# 43 ^3: 79507 sum: 93 [ 28 ]


count = 1
count_up = 1000
sum_number = 0
while count <= count_up:
    if count % 2 != 0:
        number_cubed = count ** 3
        sum_digit = 0
        while number_cubed > 0:
            sum_digit = sum_digit + number_cubed % 10
            number_cubed = number_cubed // 10
        if sum_digit % 7 == 0:
            sum_number += count
            print(count,'^3:', count**3,'sum:',sum_number,'[',sum_digit,']')
    count +=1

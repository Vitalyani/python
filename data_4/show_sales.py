from sys import argv
with open('bakery.csv', 'r', encoding='utf-8-sig') as f:
    # Нагородил я тут что-то громоздкое, но вроде все работает.
    # Скорее всего можно сделать проще и короче, но смог только так.

    # определяю длину списка введенных в консоли значений:
    length = len(argv)
    # num_lines = sum(1 for line in f) # Тут я хотел узнать количество
    # строк в файле, что бы выводить сообщение, если введенное число больше
    # количества строк в файле. Но для подсчета количества строк нужно
    # пройтись по всему файлу, а после пройтись еще раз для вывода на экран.
    # Если я правильно понял, то два цикла по одному файлу не будут работать,
    # т.к. первый цикл истощит итератор и для второго нужно будет снова
    # открывать файл.

    # если в консоле введено только "python show_sales.py",
    # то выводим весь список строк, записанных в файле:
    if length == 1:
        for line in f:
            print(line.replace('\n', ''))
    # если в консоле введено кроме "python show_sales.py" еще значение,
    # то проверяем число ли это, и выводим список строк, записанных в
    # файле, начиная с введенного значения:
    elif length == 2:
        p1 = str(argv[1])

        if not p1.isnumeric():
            print('Для вывода должно быть введено целое число')
        else:
            start = int(argv[1])-1
            f1 = f.readlines()[start:]
            for line in f1:
                print(line.replace('\n', ''))
    # если в консоле введено кроме "python show_sales.py" еще два значения,
    # то проверяем числа ли это и не превышает ли первое введенное число
    # второе число, и выводим список строк, записанных в файле, начиная с
    # первого введенного значения и заканчивая вторым значением:
    elif length == 3:
        p1 = str(argv[1])
        p2 = str(argv[2])

        if not (p1.isnumeric() and p2.isnumeric()):
            print('Должны быть введены целые числа')
        else:
            start = int(argv[1]) - 1
            finish = int(argv[2])
            if start >= finish:
                print('Первое число не должно превышать второе число')
            else:
                f2 = f.readlines()[start:finish]
                for line in f2:
                    print(line.strip())#replace('\n', ''))
    else:
        print('Количество числовых значений должно быть от 0 до 2')

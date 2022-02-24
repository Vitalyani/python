from sys import argv
with open('bakery.csv', 'a', encoding='utf-8-sig') as f:
    length = len(argv)
    if length == 1 or length > 2:
        print('необходимо ввести одно целое число')
    else:
        p = str(argv[1])
        if not p.isnumeric():
            print('введено не целое число ')
        else:
            f.write(f'{p}\n')



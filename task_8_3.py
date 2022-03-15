# 3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:
# Примеры/Тесты:
##
# def type_logger...
#     ...
#
# @type_logger
# def render_input(*args, **kwargs):
#    return 1
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# Call for: calc_cube
# 5: <class 'int'>
# Rezult: 125  type: <class 'int'>
#
# >>> render_input(1, a = 2, b = True, c = "q")
# Call for: render_input
# 1: <class 'int'>
# 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
# Rezult: 1  type: <class 'int'>
#
# Техническое задание:
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть внутри функции-обертки(декораторе)
# После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы, и возвращаемое значение остались как у исходной функции.

def type_logger(func):
    def new_func(*args, **kwargs):

        rez = func(*args, **kwargs)
        print(f'Call for: {func.__name__}')
        print(f'{int(*args)} : {type(*args)} ')

        # Дальше я вообще запутался и не понял как kwargs превратить в строку:
        # 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
        if func.__name__ == "render_input":
            print(kwargs, ':', {type(kwargs)})
            # print(*kwargs, ':', {type(kwargs)})
            # for kw in kwargs:
            #     print(kw,'=',kwargs,':',type(kwargs))

        print(f'Rezult: {rez} type: {type(*args)}')
        return rez
    return new_func

@type_logger
def render_input(*args, **kwargs):
   return 1

@type_logger
def calc_cube(x):
   return x ** 3

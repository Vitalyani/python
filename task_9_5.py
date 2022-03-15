# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Техническое задание:
#
# атрибут title (название)
# метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Сделать запись {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Начертить фигуру {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Нарисовать на доске {self.title}')

pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашом')
pencil.draw()
handle = Handle('маркером')
handle.draw()
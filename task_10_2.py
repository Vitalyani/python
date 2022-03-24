# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Формат вывода результата:
#
# Создать не менее 3 экземпляров классов с различными данными.
# Провести расчет ткани для каждого - вывести на экран
# Продемонстрировать накопительный счетчик по каждому классу.
# Техническое задание:
#
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название/имя (атрибут).
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это целые числа, например V и H, соответственно.
# Создать метод расчета ткани для каждого класса: пальто, костюм по формуле: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Выполнить общий подсчёт расхода ткани. Для всех экземпляров пальто и отдельно для всех экземпляров костюма. Алгоритм должен работать для любого кол-ва экземпляров.
# Проверить на практике полученные на этом уроке знания. Использовать абстрактный класс для «одежды» и наследование. Проверить работу декоратора @property. Не допускайте дублирования кода или спагетти-кода (кода с многочисленными проверками условий). Тщательно продумайте что должно быть данными (атрибутами), а что методами.
# Не принципиально будет ли накапливаться общий расход ткани определенным методом или будет скрыт внутри других методов/конструктора.

# from abc import ABC, abstractmethod
# class Clothes(ABC):
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     def consumption(self):
#         return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'
#     @abstractmethod
#     def abstract(self):
#         return 'Smth vary abstract'
#
# class Coat(Clothes):
#     def consumption(self):
#         return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'
#     def abstract(self):
#         return 'Smth vary abstract second'
#
# class Costume(Clothes):
#     def consumption(self):
#         return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'
#     def abstract(self):
#         pass
#
# coat = Coat(400)
# costume = Costume(55)
# print(coat.consumption())
# print(costume.consumption())
# print(coat.abstract())

from abc import ABC,abstractmethod
class Clothes(ABC):
    def __init__(self,name: str):
        self.name = name
    @abstractmethod
    def fabric_amount_calc(self):
        pass

class Coat(Clothes):
    def __init__(self, name: str, v: int):
        self.v = v
        super().__init__(name)
    @property
    def fabric_amount_calc(self):
        return round(self.v / 6.5 +0.5, 3)

class Suit(Clothes):
    def __init__(self, name: str, h: int):
        self.h = h
        # self.sum_h = []
        super().__init__(name)
    @property
    def fabric_amount_calc(self):
        return round(2 * self.h + 0.3, 3)
    # def add_fac(self, x):
    #     self.sum_h.append(self, x)
    # def total(self):
    #     total = self.h
    #     for el in self.sum_h:
    #         total += el.h
    #     return total
coat = Coat("Пальто", 48)
suit = Suit("Костюм 1", 172)

print(coat.name, coat.fabric_amount_calc)
print(suit.name, suit.fabric_amount_calc)
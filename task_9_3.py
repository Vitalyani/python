# 3. Реализовать класс Worker (работник).
# Техническое задание:
#
# определить атрибуты: name, surname, position (должность), income (доход)
# атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}
# При создании экземпляра параметры wage, bonus передаются как числа.
# создать класс Position (должность) на базе класса Worker. Это наследование.
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income). Подумайте, корректно ли в классе наследнике напрямую обращаться к защищенному атрибуту income. Или нужен getter? Аргументируйте ответ.
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, surname, name, position, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

person = Position('Иванов', 'Иван', 'программист', 100000, 15000)
print(person.get_full_name(), person.position, person.get_total_income())
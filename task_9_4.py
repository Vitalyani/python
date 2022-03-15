# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, is_police(булево). speed - текущая скорость машины.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала, остановилась, повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, name, speed, color,
                 is_police=False, velocity_limit=None):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.velocity_limit = velocity_limit

    def go(self):
        return f'Автомобиль начал движение'

    def stop(self):
        return f'Автомобиль остановился'

    def turn(self, direction):
        return f'Автомобиль повернул {direction}'

    def show_speed(self):
        if self.velocity_limit is not None and self.speed >= self.velocity_limit:
            return f'Автомобиль движется со скоростью {self.speed} км/ч\n' \
                   f'Внимание! Превышение скорости на {self.speed - self.velocity_limit} км/ч'
        else:
            return f'Автомобиль движется со скоростью {self.speed} км/ч'

    def test_drive(self):
        return f'Тест-драйв{" полицейского" if self.is_police else ""} автомобиля {self.name}, цвет {self.color}:'

class TownCar(Car):
    def __init__(self, name, speed, color, velocity_limit=60):
        self.velocity_limit = velocity_limit
        super().__init__(name, speed, color, velocity_limit=60)

class SportCar(Car): pass

class WorkCar(Car):
    def __init__(self, name, speed, color, velocity_limit=40):
        self.velocity_limit = velocity_limit
        super().__init__(name, speed, color, is_police=False, velocity_limit=40)

class PoliceCar(Car): pass

town = TownCar('Volkswagen Polo', 70, 'синий', False)
print('1:', town.test_drive(), town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop(), sep='\n')

sport = SportCar('AudiRS', 170, 'красный', False)
print('2:', sport.test_drive(), sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop(), sep='\n')

work = WorkCar('Gazelle', 130, 'серый', False)
print('3:', work.test_drive(), work.go(), work.show_speed(), work.turn('направо'), work.stop(), sep='\n')

police = PoliceCar('Skoda Rapid', 100, 'бело-синий', True)
print('4:', police.test_drive(), police.go(), police.show_speed(), police.turn('направо'), police.stop(), sep='\n')

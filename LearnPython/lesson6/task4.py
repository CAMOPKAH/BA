"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).


"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала:  {self.name}")
    def stop(self):
        print(f"Машина остановилась:{self.name}")
    def turn(self, direction):
        #direction - право, лево
        print(f"Машина повернула на {direction}")
    def show_speed(self):
        print(f"Скрость автомобиля: {self.speed}")
"""
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class TownCar(Car):
    def __init__(self, name):
        self.color = "cl_gray"
        self.name = "TownCar:" + name
        self.is_police = False
    def show_speed(self):
        if self.speed > 60: print(f"Скорость автомобиля:{self.speed}. - Превышена скорость")
        else: print(f"Скорость автомобиля:{self.speed}")

class WorkCar(Car):
    def __init__(self, name):
        self.color = "cl_green"
        self.name = "WorkCar:" + name
        self.is_police = False
    def show_speed(self):
        if self.speed > 40: print(f"Скорость автомобиля:{self.speed}. - Превышена скорость")
        else: print(f"Скорость автомобиля:{self.speed}")


class SportCar(Car):
    def __init__(self, name):
        self.color = "cl_red"
        self.name = "SportCar:" + name
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, name):
        self.color = "cl_blue"
        self.name = "PoliceCar:" + name
        self.is_police = True

sp = SportCar("LADA")
sp.go()
sp.turn("лево")
sp.speed=100
sp.show_speed()

sp.stop()

ts = TownCar("BMW")
ts.go()
ts.turn("лево")
ts.speed=100
ts.show_speed()

ts.stop()
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
 абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""
from abc import ABC, abstractmethod

class AbsDress(ABC):
    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(AbsDress):
    def __init__(self, name):
        self.sz = 0
        self.name = name

    def calc_cloth(self):
        return self.sz / 6.5 + 0.5 #(V/6.5 + 0.5)

    @property
    def size(self):
        return self.sz
    @size.setter
    def size(self, size):
        self.sz = size

class Suit(AbsDress):
    def __init__(self, name):
        self.name = name
        self.ht = 0

    def calc_cloth(self):
        return self.ht * 2 + 0.3 #(2*H + 0.3)

    @property
    def height(self):
        return self.ht
    @height.setter
    def height(self, height):
        self.ht = height

st = Coat("Пальто")
st.size = 10
print(f"Для изготовления пальто с размером {st.size} необходимо ткани: {st.calc_cloth()}")

ft = Suit("Костюм")
ft.height = 10
print(f"Для изготовления костюма с ростом {ft.height} необходимо ткани: {ft.calc_cloth()}")

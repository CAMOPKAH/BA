"""
6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
 Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
  Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
   что выведет описанный метод для каждого экземпляра.

"""

class Stationery :
    def __init__(self, title):
        self.title = title

    def Draw(self):
        print("Запуск отрисовки")

class Pen(Stationery) :
    def Draw(self):
        print(f"[{self.title}] Отрисовка шариковой ручкой")

class Pencil(Stationery):
    def Draw(self):
        print(f"[{self.title}] Отрисовка карандашом")

class Handler(Stationery):
    def Draw(self):
        print(f"[{self.title}] Отрисовка маркером")

stationery = Stationery("Канцелярская принадлежность")

stationery.Draw()

pen = Pen("Синяя гелевая ручка")
pen.Draw()

pencil = Pencil("Карандаш H2")
pencil.Draw()

handler = Handler("Красный маркер")
handler.Draw()

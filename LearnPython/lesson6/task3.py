"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
  и ссылаться на словарь, содержащий элементы: оклад и премия, например,
   {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
   В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
   и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
   (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
    вызвать методы экземпляров).

"""

class Worker:
    dic_income = ({"wage": 100000, "bonus": 70000}, {"wage": 90000, "bonus": 70000}, {"wage": 90000, "bonus": 70000})
    def __init__(self, name, surname, position, income ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_ind_dic = income
    def get_income(self):
        return self.dic_income[self._income_ind_dic]

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        x = {}
        x = self.get_income()


        return self.get_income().get("wage") + self.get_income().get("bonus")

pos1 = Position("Василий", "Иванов", "рабочий", 0 )
print(f"Полное имя рабочего 1:{ pos1.get_full_name()}")
print(f"Согласно справочнику оклада и бонуса:{pos1.get_income()}")
print(f"Доход с учётом премии:{ pos1.get_total_income()}")
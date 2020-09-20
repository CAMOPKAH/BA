"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import traceback

class Data:
    @classmethod
    def __init__(self, dt_str):

        #dt_str - дата в формате день-месяц-год
        arr = str(dt_str).split("-")
        if len(arr) != 3:
            raise ValueError(f"Ошибка: Данные не соотвествуют формату день-месяц-год")
        self.day = int(arr[0])
        self.month = int(arr[1])
        self.year = int(arr[2])

    @staticmethod
    def correct(dt_str):
        # dt_str - дата в формате день-месяц-год
        arr = str(dt_str).split("-")

        if len(arr) != 3:
            raise ValueError(f"Ошибка: Данные не соотвествуют формату день-месяц-год")
        if int(arr[0]) < 1 or int(arr[0]) > 31 : raise ValueError(f"Ошибка: день должен быть от 1..31")
        if int(arr[1]) < 1 or int(arr[1]) > 12: raise ValueError(f"Ошибка: месяц должен быть от 1..12")
        if int(arr[2]) < 1: raise ValueError(f"Ошибка день должен быть от 1..31")

    def print_date(self):
       print(f"День:{str(self.day)}\nМесяц:{str(self.month)}\nГод:{str(self.year)}")

def print_err(dt_str):
    print(f"Проверка корректности данных:{dt_str}")
    try:
        Data.correct(dt_str)
        print("Формат корректный")
    except Exception as e:
        print(f"Excepion:{traceback.format_exc()}")

# Проверка дня
print_err("40-12-2012")

#Проверка месяца
print_err("05-13-2012")

#Проверка года
print_err("15-10-2012")

#Проверка формата
print_err("15sdfsdf10-2012")


#Дата в правилном формате
print_err("15-10-2012")

dt = Data("01-11-2012")
dt.print_date()

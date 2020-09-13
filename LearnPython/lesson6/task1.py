"""

1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
 красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
 второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
   Проверить работу примера, создав экземпляр и вызвав описанный метод.

   Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
    сообщение и завершать скрипт.
"""
import time

class TrafficLight:
    cl_red = "красный"
    cl_yellow = "жёлтый"
    cl_green = "зелёный"
    cl_none = "нет"
    dic_time_color = {cl_red:7, cl_yellow:2, cl_green: 10} #Время переключения
    dic_next_color = [cl_red, cl_yellow, cl_green] #Порядок переключения
    def __init__(self):
        self.__color = self.cl_none #Сфетофор не работает
        self.__color_time_tick = 0 # Если равен нулю следуюет переключать цвет
        self.__color_next = 0 #Следующий разрешённый цвет
        print("Инициировали светофор")

    def setColor(self, new_color):
        time = self.dic_time_color.get(new_color)
        if (time == None) : raise ValueError(f"Ошибка:{new_color} - Нет такго цвета!")

        #Проверяем порядок цветов, кроме случая включения или выключения светофора
        if (new_color != self.cl_none) and (self.__color != self.cl_none) and ( new_color  != self.__color_next ): raise ValueError(f"Ошибка: установка цвета не соответствует порядку красный, жёлтый, зелёный")

        #Установка и времени работы
        self.__color = new_color
        self.__color_time_tick = time


        #переключаем цвет согласно порядку
        self.__color_next = self.dic_next_color[(self.dic_next_color.index(new_color) + 1) % len(self.dic_next_color)]
        print(f"Установлен цвет на сфетофоре: {new_color} \n Время работы:  {time} сек \n Следущий цвет: {self.__color_next}")


    def nextSecond(self):
        while (self.__color_time_tick>-1) :
            print(f"Осталось {self.__color_time_tick} сек")
            time.sleep(1)
            self.__color_time_tick = self.__color_time_tick - 1

    def running(self):

        #Проходим 1 раз
        for i in range(len(self.dic_time_color)) :
            #Установка цвета
            color=str(self.dic_next_color[i])
            print(color)
            self.setColor(color)
            #Ожидание переключения
            self.nextSecond()


TR = TrafficLight()
TR.running()

#Следующий цвет должен быть красны, для демонстрации проверки мы поставим жёлтый
TR.setColor(TR.cl_yellow)




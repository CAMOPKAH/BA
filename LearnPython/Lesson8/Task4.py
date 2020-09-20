"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

class Technic:

    #Бренд
    @property
    def brend(self):
        return self.brend_x
    @brend.setter
    def brend(self, brend):
        self.brend_x = brend

    #Кол-во в упаковке
    @property
    def pack_count(self):
        return self.pack_count_x
    @brend.setter
    def pack_count(self, pack_count):
        self.pack_count_x = pack_count

    #Вес кг
    @property
    def weight(self):
        return self.weight_x
    @weight.setter
    def pack_count(self, weight):
        self.weight_x = weight

    #Объём
    @property
    def volume(self):
        return self.volume_x

    @volume.setter
    def volume(self, volume):
        self.volume_x = volume

    #Модель
    @property
    def model(self):
        return self.model_x

    @model.setter
    def model(self, model):
        self.model_x = model


    #Цвет
    @property
    def color(self):
        return self.color_x

    @color.setter
    def color(self, color):
        self.color_x = color


#Сканнер
class Scanner(Technic):
    # Количество сканирования в минуту
    @property
    def scan_per_min(self):
        return self.scan_per_min_x

    @scan_per_min.setter
    def scan_per_min(self, scan_per_min):
        self.scan_per_min_x = scan_per_min

#Ксерокс
class Xerox(Technic):
    # Количество копий в минуту
    @property
    def copy_per_min(self):
        return self.copy_per_min_x

    @copy_per_min.setter
    def copy_per_min(self, copy_per_min):
        self.copy_per_min_x = copy_per_min


class Printer(Technic):
    # Скорость печати (страниц в минуту)
    @property
    def print_per_min(self):
        return self.print_per_min_x

    @print_per_min.setter
    def print_per_min(self, print_per_min):
        self.print_per_min_x = print_per_min


class StorePlace:
    #width_story Максимальная количесво ячеек хранения по ширене
    #height_story Максимальное кол-во ячеек по высоте
    #stends_story Количество стелажей на складе
    #MaxVCell объём одной ячейки


    def __init__(self, width_story, height_story, stends_story , max_v_cell):
        self.story_width = width_story
        self.story_height = height_story
        self.story_stends = stends_story
        self.story_MaxCell = max_v_cell

        self.story = []
        for z in range(self.story_stends):
            matrix = []
            for j in range(self.story_height):
                line = []
                for i in range (self.story_width):
                    line.append(None) #Добавляем ячейку
                matrix.append(line)  #Добавляем паллет
            self.story.append(matrix) #Добавляемс стелаж


    def cell_get(self, x, y, stend):
        if x<0 or x > self.story_width-1 or y <0 or y>self.story_height-1 or stend<0 or stend>self.story_stends-1: ValueError(f"Ячейка [{stend}:{y}:{x}] отсутствует!")
        return self.story[stend][y][x]

    def cell_set(self, x, y, stend, cell):
        if x < 0 or x > self.story_width - 1 or y < 0 or y > self.story_height - 1 or stend < 0 or stend > self.story_stends - 1: ValueError(
            f"Ячейка [{stend}:{y}:{x}] отсутствует!")
        self.story[stend][y][x] = cell


    def cell_print(self, x, y, stend):

        print(f"Ячейка:[{stend}:{y}:{x}]")
        obj = self.story[stend][y][x]
        if obj != None:
            print(obj)
            print(obj.__dict__)
        else:
            print("None")




story = StorePlace(10, 10 , 5, 10)

scan =  Scanner()
scan.brend = "HP"
scan.color = "white"
scan.pack_count = 1
scan.scan_per_min = 10
story.cell_set(1,1,2, scan)

prt = Printer()
prt.brend = "Epson"
prt.color = "black"
prt.pack_count = 2
prt.print_per_min = 20
story.cell_set(2,1,2, prt)

xerox =  Xerox()
xerox.brend = "Epson"
xerox.color = "black"
xerox.pack_count = 2
xerox.copy_per_min = 20
story.cell_set(3,1,2, xerox)


story.cell_print(3,1,2)

story.cell_print(2,1,2)

story.cell_print(1,1,1)

story.cell_print(0,1,1)




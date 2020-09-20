"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
  оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
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

        # Кол-во в упаковке

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
    def __init__(self, name):
        self.story = {}
        self.name = name

    def __str__(self):
        res = "\n##### " + self.name + " #####\n"
        for i in self.story:
            cells = self.story.get(i)
            res = res + f" <<<<< {i} >>>>>> \n"
            for j in cells:
                 res = res + f"     {str(j['src'].__class__.__name__)} Кол-во:{str(j['count'])} Параметры: {str(j['src'].__dict__)} \n"
            #self.story[i]["src"].__class__.__name__
            #res = res + f"{i} { type(self.story[i]['src']).name  } Кол-во:{self.story[i]['count']} \n"
            # Кол-во:{j['count']} {str(j['src'.__dict__])}
        return res


    def story_add(self, NameCel, technic, cnt):
        cell = self.story.get(NameCel)
        if cell == None:
            self.story[NameCel] = [{"src": technic, "count": cnt}]
        else: self.story[NameCel].append({"src": technic, "count": cnt})

    #Получаем информацию, что хранится на складе
    def story_info(self, NameCel):
        return self.story[NameCel]

    #Забираем со склада
    def story_out(self, name_cel, technic, cnt):
        lst = self.story[name_cel]
        for i in lst:
            if i.get("src").__hash__() == technic.__hash__():
                if (i["count"] - cnt < 0): raise ValueError("Техники меньше запрашиваемого количества")
                if (i["count"] - cnt == 0): lst.remove(i)
                else: i["count"] = i["count"] - cnt
                return
        raise ValueError("Техники в указанной ячейке не обнаружено")

    # story_dest склад для перемещения
    # destCell ячейка для перемещения
    def story_move(self,name_cel, technic, cnt, dest_cell, story_dest):
        #Забираем с одного склада
        self.story_out(name_cel, technic , cnt)

        #Добавляем в другой
        story_dest.story_add(dest_cell, technic, cnt)


"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
  оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""







story = StorePlace("Склад")

scan =  Scanner()
scan.brend = "HP"
scan.color = "white"
scan.pack_count = 1
scan.scan_per_min = 10


prt = Printer()
prt.brend = "Epson"
prt.color = "black"
prt.pack_count = 2
prt.print_per_min = 20



xerox =  Xerox()
xerox.brend = "Epson"
xerox.color = "black"
xerox.pack_count = 2
xerox.copy_per_min = 20

story.story_add("A1", xerox, 5)
story.story_add("A2", prt, 5)
story.story_add("A2", scan, 5)

print(story)

#Подразделения компании такой же склад

company = StorePlace("Подразделения компании")

#Перемещаем со склада в подразделение принтер, сканер

print(story.story_info("A2"))

print("Перемещаем принтер и сканер в подразделения")

story.story_move("A2", prt,5, "Подразделение ДИТ" ,company)
story.story_move("A2", scan,5, "Подразделение HR" ,company)


print()
print("Техника в департаментах:", company)


print("Перемещаем 3 принтера на склад в ячейку Б2")
company.story_move("Подразделение ДИТ", prt,3, "Б2" , story)


print("На складе:", story)
print("Техника в департаментах:", company)



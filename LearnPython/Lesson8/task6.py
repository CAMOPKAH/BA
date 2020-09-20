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

#Заполнение параметров класса
class InputClass:
    @staticmethod
    def Correct(num):
        try:
            x = int(num)
        except Exception:
            return False
        return True

    @staticmethod
    def get_num(title):
        while True:
            a = input(f"Введите {title} (не отрицательное число) или stop для выхода: ")
            if a == "stop": return None
            if InputClass.Correct(a) and int(a) >-1 : return a

            else : print(f"Введённое значение '{a}' не является не отрицательным числом")

    @staticmethod
    def get_str(title):
        while True:
            a = input(f"Введите {title} (текст) или stop для пропуска: ")
            if a == "stop": return None
            return a


    @staticmethod
    def get_list_obj(title, lst):
        while True:
            c = 0
            str = title + "\n"
            for i in lst:
                str = str + f"{c} : {i.__class__.__name__}\n"
                c = c + 1
            print(str)
            a = input(f"Введите номер из списка или stop для выхода: ")
            if a == "stop": exit(0)
            if InputClass.Correct(a):
                if int(a)>-1 and int(a) < c: break
                else:  print(f"Введённое значение должнобыть в диапозоне[0;'{c-1}]'")
            else:
                print(f"Введённое значение '{a}' не является числом")


        return lst[int(a)]

    @staticmethod
    def get_list_txt(title, lst):
        while True:
            c = 0
            str = title + "\n"
            l = []
            for i in lst:
                str = str + f"{c} : {lst[i]}\n"
                l.append(i)
                c = c + 1
            print(str)
            a = input(f"Введите номер из списка или stop для выхода: ")
            if a == "stop": exit(0)
            if InputClass.Correct(a):
                if int(a) > -1 and int(a) < c:
                    break
                else:
                    print(f"Введённое значение должнобыть в диапозоне[0;'{c - 1}]'")
            else:
                print(f"Введённое значение '{a}' не является числом")

        return l[int(a)]

    @staticmethod
    def get_cur_obj(title, lst):
        print(InputClass.get_list_obj_menu(title, lst))
        i = InputClass.get_num(" номер из списка ")
        return

"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
  оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""




#Номенклатура
nomen=[]


scan =  Scanner()
scan.brend = "HP"
scan.color = "white"
scan.pack_count = 1
scan.scan_per_min = 10
nomen.append(scan)

prt = Printer()
prt.brend = "Epson"
prt.color = "black"
prt.pack_count = 2
prt.print_per_min = 20
nomen.append(prt)


xerox =  Xerox()
xerox.brend = "Epson"
xerox.color = "black"
xerox.pack_count = 2
xerox.copy_per_min = 20
nomen.append(xerox)

storys=[]
story = StorePlace("Склад")
storys.append(story)
#Подразделения компании такой же склад
company = StorePlace("Подразделения компании")
storys.append(company)


story.story_add("A1", xerox, 5)
story.story_add("A2", prt, 5)
story.story_add("A2", scan, 5)

print(story)



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


menu = {"inp":"Приход товара", "mov":"Перемещение товара","print":"Печать" , "exi":"Выход"}
while True:
    x = InputClass.get_list_txt("Меню", menu)
    if x == "exi":
        exit(0)
    if x == "inp":
        print("Приход товара")
        obj = InputClass.get_list_obj("Выберите товар для поступления", nomen)
        if obj == None: continue
        cont = InputClass.get_num(" количество ")
        if cont == None: continue
        place = InputClass.get_str(" ячейку склада( пример A2) ")
        if place == None: continue
        story.story_add(place, obj, cont)
    if x == "print":

        x = InputClass.get_list_txt("Выберите склад для печати ", {0:storys[0].name, 1:storys[1].name})
        print(storys[x])

    if x == "mov":
        print("Перемещение")
        l_tst = ["ячейка склада (приме А2)", "подразделение (пример Подразделение ДИТ) "]

        src_x = InputClass.get_list_txt("Выберите склад от куда перемещаем ", {0:storys[0].name, 1:storys[1].name})
        if src_x == None: continue
        src_cell = InputClass.get_str(l_tst[src_x])
        if src_cell == None: continue
        obj = InputClass.get_list_obj("Выберите товар для перемещения", nomen)
        if obj == None: continue
        cont = InputClass.get_num(" количество ")
        if cont == None: continue

        dst_x = InputClass.get_list_txt("Выберите склад от куда перемещаем ", {0: storys[0].name, 1: storys[1].name})
        if dst_x == None: continue
        dst_cell = InputClass.get_str(l_tst[dst_x])
        if src_cell == None: continue


        try:
            print("Операция перемещения:")
            storys[src_x].story_move(src_cell , obj, int(cont), dst_cell, storys[dst_x])
        except Exception as e:
            print(e)





"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


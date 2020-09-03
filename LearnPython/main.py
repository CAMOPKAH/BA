
list7 = []
while True:
    list7.append(
        (input("Номер товара >> "),
         {"Название": input("Название >>> "), "Цена": input("Цена >>> "), "Количество": input("Количество >>> "), "ед.": input("Единицы учёта >>> ")}
         )
    )
    q = input("Закончить ввод позиций? Да, Нет >>> ")
    if q == "Да":
        break
for el in list7:
    print(list7)


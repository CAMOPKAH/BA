"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32

"""

print("Часть 1")
"""

 !?! В ТЗ фигурируют 2 разных термина оклад и средний доход. Предполагаю, что "доход"="оклад". В жизни нужно уточнить у заказчика 
"""
cnt = 0 #общие кол-во сотрудников
sum_pay = 0 #сумма окладов
file_r = open("filePersons.txt", "r")
list_20 = []
for line in file_r:
    arr = line.replace("\n" , "").split(";")
    pay = int(arr[1].replace(" " , ""))
    cnt = cnt + 1
    sum_pay = sum_pay + pay
    if pay < 20000:
        list_20.append({"ФИО": arr[0], "Оклад": pay})
file_r.close()
print("Сотрудники получающие меньше 20 т.р.")
print(list_20)
print("Средний оклад сотрудников:", int( sum_pay / cnt ))


"""

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
print("Часть 2")

file_translate = "TranslateMatrix.txt"
#Процедура загрузки матрицы перевода
def Load_translate(NameTraslate):
    file_translate = open("TranslateMatrix.txt", "r")
    res=[]
    for line in file_translate:
        res.append(line.replace("\n", "").split(";"))
    file_translate.close()
    return res

def Translate(Matrix, inp):
    res = str(inp)
    for trn in Matrix:
        res = res.replace( trn[1], trn[2] ).replace(str(trn[1]).title(), str(trn[2]).title() ) #Переводим в соответсвии с первой буквой
    return res

#Загружаем матрицу перевода
translate_matrix = Load_translate("TranslateMatrix.txt")

#Открываем исходный файл
file_inp = open("trn_file_inp.txt", "r")
#Открываем файл для результата
file_out = open("trn_file_out.txt", "w")
for line in file_inp:
    file_out.write(Translate(translate_matrix , line)) #Построчно переводим строки
file_inp.close()
file_out.close()

# Результат
"""
Один — 1
Два — 2
Три — 3
Четыре — 4
"""







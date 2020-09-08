"""
4. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
from random import randrange

file_name = "gen_num.txt"
count_range = 100

#Генерируем файл
gen_file = open (file_name, "w")
for i in range(count_range):
    gen_file.write(str(randrange(count_range)) + " ")
gen_file.close()

#Открываем на чтение для подсчёта
r_file = open (file_name)
ssum = 0
for s_num in r_file.readline().split(" "):
    if len(s_num)>0:
        ssum = ssum + int(s_num)

print(F"Сумма в сгенерированном файле: {ssum}")
"""
 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""

f_read = open ("test_words.txt", "r")
word_count = 0
line_count = 0;
for line in f_read:
    line_count = line_count + 1
    str = " " + line.replace("\n", "") + " "  #Обрамляем в пробелами и удаляем перевод каретки
    while str.count("  ") > 0:  #Удаляем двойные пробелы
        str = str.replace("  ", " ")
    word_count = word_count + str.count(" ") -1
print(F"Кол-во строк: {line_count}\n Кол-во слов: {word_count}")
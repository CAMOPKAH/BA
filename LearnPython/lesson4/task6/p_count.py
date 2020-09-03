from itertools import count

#Генератор списка из целых чисел
def gen_count_list(start, end):
    #start начальное значение для генератора
    #end конечное значение для генератора
    list=[]
    for i in count(start):
        list.append(i)
        if i > end-1:
            break
    return list
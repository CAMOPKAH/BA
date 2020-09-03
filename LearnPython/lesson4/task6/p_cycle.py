from itertools import cycle

#Генератор списка из щаблона
def gen_pattern_list(text, count_el):
    #text текст для генератора
    #count_el кол элементов для генератора
    list=[]
    cnt = 0
    for i in cycle(text):
        cnt = cnt +1
        list.append(i)
        if cnt > count_el-1:
            break
    return list
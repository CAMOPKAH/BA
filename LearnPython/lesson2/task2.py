"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

"""
print ( "Пример ввода 12;777;dddd;fff" )
inp_string = input ( 'Введите занчения массива через ";" :' )
inp_list = inp_string.split(";")
print( "Вы ввели массив из ", len ( inp_list ) , " элементов:" )
print(inp_list)

for i in range(len(inp_list)//2):
    a = inp_list[ i * 2 + 1];
    inp_list[i * 2 + 1] = inp_list[(i)*2]
    inp_list[(i) * 2] = a
print("В результате обмена соседних элементов получаем:")
print(inp_list)
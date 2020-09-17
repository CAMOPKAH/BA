"""

1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    matr = [[]]
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        s_res = ""
        for i in self.matr:
            s_res = s_res + str(i) + "\n"
        return s_res

    def __add__(self, other):
        new_matr = [[]]
        for j in range( len(self.matr)):
            line = []
            for i in range(len(self.matr[j])):
                line.append(self.matr[j][i] + other.matr[j][i])
            new_matr.append(line)
        return Matrix(new_matr)
    def print_matr(self):
        print(self.matr)


mat = Matrix([[1,2,3],[4,5,6],[7,8,9]])
mat.print_matr() #Данные предзаполнены в методе __init__
print(mat) #перезагрузка оператора __str__
mat2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])

print("Sum matrix")
print(mat)

print("   +   ")
print(mat2)
print("   =   ")
print(mat + mat2)

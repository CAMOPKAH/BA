"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
 реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
 создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
  Проверьте корректность полученного результата.
Важно!
"""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
    def __str__(self):
        str = ""

        if int(self.b) > -1: str =  "+"
        return f"{self.a}{str}{self.b}i"


c1 = Complex(2, 1)
c2 = Complex(3, 5)
print(c1 + c2) #5+6i

print(Complex(3, 1) * Complex(2, -3)) #9-7i


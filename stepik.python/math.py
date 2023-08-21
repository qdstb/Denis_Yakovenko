import math 

num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

n1 = math.factorial(2)
print(n1)

# Напишите программу, вычисляющую значение тригонометрического выражения
from math import sin, cos, tan, radians
x = radians(float(input()))

print(sin(x) + cos(x) + (tan(x)**2))

from math import sqrt
a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if d < 0:
    print("Нет корней")
if d == 0:
    print(-b / (2 * a))
if d > 0:
    k1 =(-b - sqrt(d)) / (2 * a)
    k2 =(-b + sqrt(d)) / (2 * a)
    if k1 < k2:
        print(k1, k2, sep="\n")
    else:
        print(k2, k1, sep="\n")


from math import pi, tan

n = float(input())
a = float(input())

print((n * a ** 2) / (4 * tan(pi / n)))

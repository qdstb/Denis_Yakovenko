s = input()

for i in range(10):
    print(i,s)

s = int(input())

for i in range(s+1):
    print("Квадрат числа", i, "равен", i**2)


# Программа должна вывести треугольник в соответствии с условием задачи.
s = int(input())

for i in range(s):
    print("*" * s)
    s -= 1

n = int(input())

for i in range(n):
    print("*" * (n - i))



# Напишите программу, которая предсказывает размер популяции 
# организмов. Программа должна выводить размер популяции в каждый 
# день, начиная с 1 и заканчивая n-м днем.


m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print( i + 1, m * (1 + p / 100) ** i)


num = int(input())
p = int(input())
days = int(input())
for x in range(days):
    print(x + 1, num)
    num = num + p / 100 * num

#Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n
# включительно в порядке возрастания, если m<n, 
# или в порядке убывания в противном случае.

m =int(input())
n =int(input())

if m < n:
    for i in range (m, n+1):
        print(i)
else:
    for i in range (m, n-1, -1):
        print(i)


m =int(input())
n =int(input())

for i in range (m, n-1, -1):
    if i % 2 != 0:
        print(i)
    

m =int(input())
n =int(input())

for i in range(m, n+1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)


n =int(input())

for i in range(1, 10+1):
        print(n, "x", i, "=", n * i)

#На вход программе подаются два целых числа a и b(a≤b).
# Напишите программу, которая подсчитывает количество чисел
#  в диапазоне от a до b включительно, куб которых оканчивается на 
# 4 или 9.
a = int(input())
b = int(input())
count = 0

for i in range(a, b+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)

#На вход программе подается натуральное число n, а затем
# n целых чисел, каждое на отдельной строке.
#  Напишите программу, которая подсчитывает сумму введенных чисел. 
sm = 0
for i in range(int(input())):
    n = int(input())
    sm += n
print(sm)


# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение выражения
from math import log 

n = int(input())
count = 0

for i in range(1, n+1):
    count += 1 / i

print(count - log(n))


#На вход программе подается натуральное число n.
#  Напишите программу, которая подсчитывает сумму тех чисел от 
# 1 до n (включительно), квадрат которых оканчивается на 
# 2,5 или 8.

n = int(input())
count = 0
for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        count += i
print(count)
     
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет Факториал !n     

n = int(input())
count = 1
for i in range(1, n+1):
    count *= i
print(count)

# Напишите программу, которая считывает 10 чисел
# и выводит произведение отличных от нуля чисел.

count = 1
for i in range(10):
    n = int(input())
    if n != 0:
        count *= n

print(count)

# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.

n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += i
print(count)

# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы 

n = int(input())
count = 0
for i in range(1, n + 1):
    count += (-1) ** (i + 1) * i

print(count)

# На вход программе подается натуральное число n.
# а затем n различных натуральных чисел последовательности,
#  каждое на отдельной строке. Напишите программу,
#  которая выводит наибольшее и второе наибольшее
#  число последовательности.

max = 0
sec = 0

for i in range(int(input())):
    n = int(input())
    if n > max:
        sec = max
        max = n
    elif n > sec and n < max:
        sec = n
print(max, sec, sep="\n")

# Напишите программу, которая считывает последовательность из 10
# целых чисел и определяет является ли каждое из них четным или нет

count = 0
for i in range(10):
    n = int(input())
    if n % 2 != 0:
        count += 1

if count == 0:
    print("YES")
else:
    print("NO")

# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Фибоначчи.

n = int(input())
a1 = 0
a2 = 1
for i in range(n):
    c = a1 + a2
    a1 = a2
    a2 = c
    print(a1 , end=" ")
    

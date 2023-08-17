age = int(input())
print('Доступ разрешен' if age >= 18 else 'Доступ запрещен')

number = int(input())
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number <= number_1:
    min_N = number
else:
    min_N = number_1
    
if min_N <= number_2:
    minN_1 = min_N
else:
    minN_1 = number_2
    
if minN_1 <= number_3:
    print(minN_1)
else:
    print(number_3)

# Для решения задачи нужно разбить 4 числа a, b, c, d на 2 пары: a, b и c, d.
# Далее находим максимум в каждой паре,
# а затем среди этих двух максимумов выбираем максимальное =)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)

age = int(input())
if age < 14:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
i = 0
if n_1 > 0:
    i += n_1
    
if n_2 > 0:
    i += n_2

if n_3 > 0:
    i += n_3
    
print(i)


print("Принадлежит" if 0 <= int(input()) <= 16 else "Не принадлежит")

# Напишите программу, которая принимает целое число x
# и определяет, принадлежит ли данное число указанным промежуткам.
if -3 < int(input()) < 7:
    print('Не принадлежит')
else:
    print('Принадлежит')

#если оно является четырехзначным и делится нацело на 7 или 17
x = int(input())

print("YES" if 999 < x < 10000 and (x % 7 == 0 or x % 17 == 0) else "NO")

# Ход короля
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((x1 - x2) == 0 or (x1 - x2) == - 1 or (x1 - x2) == 1) and ((y1 - y2) == 0 or (y1 - y2) == - 1 or (y1 - y2) == 1):
    print("YES")
else:
    print("NO")


#ладья

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
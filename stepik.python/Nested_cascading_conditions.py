# Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно вывести "Don't know".
print('YES' if (k := int(input())) < (n := int(input())) else 'NO' if k > n else "Don't know")

#среднее из 3

n1 = int(input())
n2 = int(input())
n3 = int(input())
if n2 < n1 < n3 or n2 > n1 > n3:
    print(n1)
elif n1 < n2 < n3 or n1 > n2 > n3:
    print(n2)
else:
    print(n3)
# кол-во дней по месяцу
mounth = int(input())

if mounth == 2:
    print(28)

elif mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11:
    print(30)

else:
    print(31)

# Программа должна вывести результат применения операции к введенным числам
# или соответствующий текст, если операция неверная либо если происходит деление на ноль.

n1 = int(input())
n2 = int(input())
o = input()

if o == "/":
    if  n2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(n1 / n2)
elif o == "+":
    print(n1 + n2)
elif o == "-":
    print(n1 - n2)
elif o == "*":
    print(n1 * n2)
else:
    print("Неверная операция")

# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.
c1, c2 = input(), input()

if c1 == 'красный' and c2 == 'синий' or c1  == 'синий' and c2 == 'красный':
    print('фиолетовый')
elif c1 == 'красный' and c2  == 'желтый' or c1 == 'желтый' and c2  == 'красный':
    print('оранжевый')
elif c1 == 'синий' and c2  == 'желтый' or c1 == 'желтый' and c2  == 'синий':
    print('зеленый')
elif (c1 == 'синий' or c1 == 'красный' or c1 == 'желтый') and c1 == c2 :
    print(c1)
else:
    print('ошибка цвета')


# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный
n = int(input())
if n < 0 or n > 36:
    print("ошибка ввода")
elif n == 0:
    print("зеленый")

if 1 <= n <= 10 or 19 <= n <= 28:
    if  n % 2 == 0:
        print("черный")
    else:
        print("красный")

if 11 <= n <= 18 or 29 <= n <= 36:
    if  n % 2 == 0:
        print("красный")
    else:
        print("черный")

# пересечение отрезков
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 < a2 or b2 < a1:
    print("пустое множество")
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a2 > a1 and b1 < b2:
    print(a2, b1)
elif a2 < a1 and b2 < b1:
    print(a1, b2)

elif a1 >= a2 and b1 <= b2:
    print(a1,b1)

elif a2 >= a1 and b2 <= b1:
    print(a2,b2)
# Шахматная доска На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if ((a1 + b1) % 2 == 0 and (a2 + b2) % 2 == 0) or ((a1 + b1) % 2 != 0 and (a2 + b2) % 2 != 0):
    print("YES")
else:
    print("NO")
# короткое решение
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a + b + c + d) % 2 == 0:
    print('YES')
else:
    print('NO')
# римские цифры
n = int(input())
d1 = "I"
d2 = "V"
d3 = "X"
if n < 1 or n > 10:
    print("ошибка")
elif 1 <= n <= 3:
    print(n*d1)
elif n == 4:
    print(d1+d2)
elif 5 <= n <= 8:
    print(d2 + (n % 5) * d1)
elif n == 9:
    print(d1+d3)
elif n == 10:
    print(d3)

# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO»
n = int(input())

if n % 2 != 0:
    print("YES")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("NO")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("YES")
elif n % 2 == 0 and n > 20:
    print("NO")

#ход слона  
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 + b1) == (a2 + b2) or (a1 - a2) == (b1 - b2):
    print("YES")
else:
    print("NO")

#ход коня

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 - a2) * (b1 - b2) == 2 or (a1 - a2) * (b1 - b2) == -2:
    print("YES")
else:
    print("NO")


# Ход ферзя
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

#слон
if (a1 + b1) == (a2 + b2) or (a1 - a2) == (b1 - b2):
    print("YES")
#король
elif ((a1 - a2) == 0 or (a1 - a2) == - 1 or (a1 - a2) == 1) and ((b1 - b2) == 0 or (b1 - b2) == - 1 or (b1 - b2) == 1):
    print("YES")
#ладья
elif a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")

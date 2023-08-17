a = int(input())
b = int(input())

print(3*(a+b)**3+275*b**2 - 127 * a - 41)

monitor = int(input())
sys = int(input())
keyboard = int(input())
mouse = int(input())
print(sum([monitor+sys+keyboard+mouse]*3))

print(15 // (16 % 7))

n = int(input())-1
print(n)
students = int(input())
mandarins = int(input())
print(mandarins // students)
print(mandarins % students)

population = int(input())
print(population // 2 + population % 2 )

number = int(input())
print (-(-number // 4))

#для чайников:

123456789  // 1 % 10 #---> 9        (единицы)

123456789   // 10 % 10 #---> 8      (десятки)

123456789  // 100 % 10 #---> 7      (сотни)

123456789  // 1000 % 10 #---> 6     (тысячи)

123456789  // 10000 % 10 #---> 5    (десятки тысяч)

123456789  // 100000 % 10 #---> 4   (сотни тысяч)

123456789  // 1000000 % 10 #---> 3  (миллионы)

123456789  // 10000000 % 10 #---> 2 (десятки миллионов)

123456789  // 100000000 % 10 #---> 1 (сотни миллионов)

#и т. д.
#сам обнаружил этот способ для меня он гораздо удобней чем то что представлено

number = int(input())
units = number // 1 % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
print("Сумма цифр =", units + tens + hundreds)
print("Произведение цифр =", units * tens * hundreds)

# abc,acb,bac,bca,cab,cba.

a,b,c = input()
print(a,b,c,'\n',a,c,b,'\n',b,a,c,'\n',b,c,a,'\n',c,a,b,'\n',c,b,a, sep="" )

from itertools import *

for i in permutations(input()):
	print(''.join(i))

a,b,c,d = input()
stroka1 = "Цифра в позиции "
stroka2 = "равна "
print(
stroka1 + "тысяч" + stroka2, a,'\n',
stroka1 + "сотен" + stroka2, b,'\n',
stroka1 + "десятков" + stroka2, c,'\n',
stroka1 + "единиц" + stroka2, d,'\n', sep=""
)

a,b,c,d = input()
print(f"Цифра в позиции тысяч равна {a}",
        f"Цифра в позиции сотен равна {b}",
        f"Цифра в позиции десятков равна {c}",
        f"Цифра в позиции единиц равна {d}", sep='\n')

star = "*"
gap = " "
print(star*17)
print(star, gap*13, star)
print(star, gap*13, star)
print(star*17)

number_1 = int(input())
number_2 = int(input())
print("Квадрат суммы", number_1, "и", number_2, "равен", (number_1 + number_2)**2)
print("Сумма квадратов", number_1, "и", number_2, "равна", number_1**2 + number_2**2)

n = int(input())
n_2 = str(n)
print(n + int(n_2 * 2) + int(n_2 * 3))

number = list(map(int, input()))
if number[0] + number[3] == number[1] - number[2]:
    print("ДА")
else:
    print("НЕТ")


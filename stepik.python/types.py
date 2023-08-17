#Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

print(int(float(input()) * 10) % 10)

n = float(input())
print (n - int(n))

a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input())
print(f"Наименьшее число = {min(a, b, c, d, e)}\n"
      f"Наибольшее число = {max(a, b, c, d, e)}")

n1 = int(input())
n2 = int(input())
n3 = int(input())
min = min(n1,n2,n3)
max = max(n1,n2,n3)
print(min, (n1 + n2 + n3) - (max + min),max, sep='\n')

# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине
#  цифре. Напишите программу, которая определяет, интересное число или нет. Если число интересное, следует
#  вывести «Число интересное», иначе - «Число неинтересное».

n = int(input())
d1 = n % 10
d2 = n // 10 % 10
d3 = n // 100 % 10
max = max(d1, d2, d3)
min = min(d1, d2, d3)
print("Число интересное" if max - min == (d1 + d2 + d3) - (max + min) else "Число неинтересное")

n = int(input())
n1 = n // 10 ** 0 % 10
n2 = n // 10 ** 1 % 10
n3 = n // 10 ** 2 % 10

if n1 + n2 + n3 == 2 * max(n1, n2, n3):
    print("Число интересное")
else:
    print("Число неинтересное")

n1 = abs(float(input()))
n2 = abs(float(input()))
n3 = abs(float(input()))
n4 = abs(float(input()))
n5 = abs(float(input()))

print(n1 + n2 + n3 + n4 + n5)

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
print(abs(n1 - n3) + abs(n2 - n4))
print(f"Hello {input()} {input()}! You have just delved into Python")

s = input()
print(f"Футбольная команда {s} имеет длину {len(s)} символов")

# Даны названия трех городов. Напишите программу, которая определяет самое #  короткое и самое длинное название города.


c1 = input()
c2 = input()
c3 = input()
l1 = len(c1)
l2 = len(c2)
l3 = len(c3)

if l1 < l2 and l1 < l3:
    if l2 < l3:
        print(c1, c3, sep ="\n")
    else:
        print(c1, c2, sep ="\n")

if l2 < l1 and l2 < l3:
    if l1 < l3:
        print(c2, c3, sep ="\n")
    else:
        print(c2, c1, sep ="\n")

if l3 < l1 and l3 < l2:
    if l1 < l2:
        print(c3, c2, sep ="\n")
    else:
        print(c3, c1, sep ="\n")

a, b, c = input(), input(), input()

if len(a) < len(b): 
    b, a = a, b

if len(b) < len(c): 
    c, b = b, c

if len(a) < len(b): 
    b, a = a, b

print(c, a, sep='\n')

# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
c1 = input()
c2 = input()
c3 = input()
l1 = len(c1)
l2 = len(c2)
l3 = len(c3)


l1 = len(input())
l2 = len(input())
l3 = len(input())
min = min(l1, l2, l3)
max = max(l1, l2, l3)
mid = (l1 + l2 + l3) - (max + min)
if max - mid == mid - min:
    print("YES")
else:
    print("NO")


c1 = input()
print("YES" if "суббота" in c1 or "воскресенье" in c1 else "NO")
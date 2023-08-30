counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)


# Дано натуральное число n <= 9 Напишите программу,
# которая печатает таблицу размером n x 3
# состоящую из данного числа (числа отделены одним пробелом).

n = int(input())

for i in range(n):
    for j in range(1):
        n1 = str(n)
        print(n1, n1 ,n1, sep=" ", end="\n")

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
    


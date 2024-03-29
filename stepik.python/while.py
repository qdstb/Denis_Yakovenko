#На вход программе подается последовательность слов,
#  каждое слово на отдельной строке.
#  Концом последовательности является одно из трех слов:
#  «стоп», «хватит», «достаточно» 
# (маленькими буквами, без кавычек).
#  Сами эти слова в последовательность
#  не входят, лишь символизируя её окончание.
#  Напишите программу, которая выводит
#  общее количество членов данной последовательности.

text = input()
c = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    
    text = input()
    c += 1
print(c)

# Программа должна вывести члены данной последовательности.
# Концом последовательности является любое число, не делящееся на 7
n = int(input())

while n % 7 == 0:
    print(n)
    n = int(input())

#Программа должна вывести сумму членов данной последовательности.

n = int(input())
c = 0
while n >= 0:
    c += n
    n = int(input())

print(c)
    
# Количество пятерок (инпут в цикле после if
#  чтобы засчитало последнюю 5ку)

n = int(input())
c = 0
while n > 0 and n < 6:
    
    if n % 5 == 0:
        c += 1
    n = int(input())

print(c)

#На вход программе подается одно натуральное число
#  - цена за услугу ведьмака.
#Программа должна вывести минимально возможное количество
#  чеканных монет для оплаты.

n = int(input())
count = 0

while n >= 25:
    n -= 25
    count += 1
while n >= 10:
    n -=10
    count += 1
while n >= 5:
    n -= 5
    count += 1

print(count + n)

#Дано натуральное число. Напишите программу,
#  которая выводит его цифры в столбик в обратном порядке.

n = int(input())
while n != 0:
    print(n % 10)
    n //= 10

# Дано натуральное число. Напишите программу,
# которая меняет порядок цифр числа на обратный.

n = int(input())
c = ""

while n != 0:
    dig = str(n % 10)
    c += dig
    n //= 10

print(int(c))

n = int(input())
new_n = 0

while n > 0:
    new_n = new_n * 10 + n % 10
    n //= 10
    
print(new_n)

# Дано натуральное число n >= 10. Напишите программу,
# оторая определяет его максимальную и минимальную цифры.

n = int(input())
ma = 0
mi = 9
while n > 0:
    dig = n % 10
    if dig > ma:
        ma = dig
    if dig < mi:
        mi = dig
    n //= 10

print("Максимальная цифра равна", ma)
print("Минимальная цифра равна", mi)


n = int(input())
max_digit = 0
min_digit = 9

while n > 0:
    cur_digit = n % 10
    
    max_digit = max(max_digit, cur_digit)
    min_digit = min(min_digit, cur_digit)
    
    n //= 10
    
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)


# Дано натуральное число. Вычислите:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

n = int(input())
sum = 0
aot = 0
mult = 1
l_d = n % 10
while n > 0:
    d = n % 10
    sum += d
    aot += 1
    mult *= d
    n //= 10 

print(sum)
print(aot)
print(mult)
print(sum / aot)
print(d)
print(d + l_d)

# Дано натуральное число n. 
# Напишите программу, 
# которая определяет его вторую (с начала) цифру.

n = int(input())
sd = 0
while n > 9:
    sd = n % 10
    n //= 10
print(sd)

n = int(input())
while n > 99:
    n //= 10

second_digit = n % 10
print(second_digit)

# Дано натуральное число. Напишите программу, которая определяет,
#  состоит ли указанное число из одинаковых цифр.

n = int(input())
fd = n % 10
flag = True
while n != 0:
    sd = n % 10
    if fd != sd:
        flag = False
    n //= 10
    
print("YES" if flag == True else "NO")


# Дано натуральное число. Напишите программу, которая определяет,
#  является ли последовательность его цифр при просмотре
#  справа налево упорядоченной по неубыванию.

n = int(input())
flag = True

while n > 9:
    d = n % 10
    d2 = n // 10 % 10
    if d > d2:
        flag = False
    n //= 10

print("YES" if flag == True else "NO")
        
# На вход программе подается число n > 1.Напишите программу,
# которая выводит его наименьший отличный от 1 делитель.

n = int(input())

for i in range(2, n+1):
    if n % i == 0:
        break

print(i)

# На вход программе подается число n > 1.Напишите программу,
# которая выводит числа от 1 до n включительно за исключением:
# от 5 до 9 / 17 - 37 / 78 - 87

n = int(input())

for i in range(1, n+1):

    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)


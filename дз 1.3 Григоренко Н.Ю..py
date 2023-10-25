a = int(input("Введите число: "))
b = 0
print("Результат:", end = " ")
for i in range(2, a - 1):
    if (a % i == 0):
        b = b+1
if (b <= 0):
    print("Число простое")
for i in range(a -1, 1, -1):
    b = 0
    if (a % i == 0):
        for c in range(i-1, 1, -1):
            if (i % c == 0):
                b = b + 1
        if (b == 0):
            print(i, end = " ")
            


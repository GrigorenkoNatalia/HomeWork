fib1 = 1
fib2 = 1
 
n = int(input("Введите число N: "))
 
i = 0
while i < n - 2:
    fib_n = fib1 + fib2
    fib1 = fib2
    fib2 = fib_n
    i = i + 1
 
print("N-ое число последовательности Фибоначчи:", fib2)
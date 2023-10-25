a = int(input("Введите размер 1 стороны: "));
b = int(input("Введите размер 2 стороны: "));

[print(*range(i,a*b+1, a)) for i in range(1, a+1)]

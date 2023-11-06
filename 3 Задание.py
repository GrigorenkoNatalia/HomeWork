#функция преобразует число из заданной системы счисления base в десятичное число
def to_decimal(number, base):
    decimal_number = 0 #для хранения значения в десятичной системе счисления
    power = 0#для отслеживания позиции текущего разряда.
    while number > 0:
        digit = number % 10#находим остаток от деления number на 10, который представляет последний разряд числа 
        decimal_number += digit * (base ** power)#увеличивается на значение текущей цифры, умноженной на основание в степени power
        number //= 10#Последняя цифра удаляется из number
        power += 1
    return decimal_number#Функция возвращает результат в десятичной системе

def from_decimal(decimal_number, new_base):
    result = ""#для хранения результата в новой системе счисления
    while decimal_number > 0:
        remainder = decimal_number % new_base#remainder как остаток от деления decimal_number на new_base
        result = str(remainder) + result#remainder преобразуется в строку и добавляется в начало result
        decimal_number //= new_base
    return result#Когда decimal_number становится равным 0, функция возвращает result, представляющий число в новой системе счисления

# Ввод основания и чисел
base_input = int(input("Введите основание исходной системы счисления: "))
number1_input = int(input("Введите первое число в системе счисления с основанием " + str(base_input) + ": "))
number2_input = int(input("Введите второе число в системе счисления с основанием " + str(base_input) + ": "))
new_base = int(input("Введите новое основание системы счисления: "))

# Перевод в десятичную систему
decimal_number1 = to_decimal(number1_input, base_input)
decimal_number2 = to_decimal(number2_input, base_input)

# Выполнение операции (в данном случае, сложение)
result_decimal = decimal_number1 + decimal_number2

# Перевод обратно в новую систему счисления
result_in_new_base = from_decimal(result_decimal, new_base)

# Вывод результата
print("Результат сложения в новой системе счисления:", result_in_new_base)

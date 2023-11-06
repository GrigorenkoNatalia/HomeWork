import string

def capitalize_letters(input_string):#Эта функция использует метод str.maketrans() для создания таблицы перевода, которая преобразует все строчные буквы входной строки в заглавные буквы
    translation_table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    return input_string.translate(translation_table)

def invert_case(input_string):#Эта функция создает таблицу перевода, которая инвертирует регистр каждой буквы во входной строке. То есть, заглавные буквы становятся строчными, а строчные буквы - заглавными.
    translation_table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                      string.ascii_uppercase + string.ascii_lowercase)
    return input_string.translate(translation_table)

def to_lowercase(input_string):#Функция преобразует все буквы во введенной строке в нижний регистр с использованием
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    translation_table = str.maketrans(uppercase_letters, lowercase_letters)
    return input_string.translate(translation_table)


word = input("Введите слово на латинском: ")
capitalized_word = capitalize_letters(word)#Здесь слово переводится в верхний регистр
invert_word = invert_case(word)#Слово, введенное пользователем, имеет инвертированный регистр
to_lowercase_word = to_lowercase(word)#Слово преобразуется в нижний регистр
print("Преобразованное слово:", capitalized_word)
print("Преобразованное слово:", invert_word)
print("Преобразованное слово:", to_lowercase_word)

import string

def capitalize_latin(input_str):
    # Создаем словарь для замены символов
    translation_dict = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    
    # Используем метод translate для преобразования букв
    result = input_str.translate(translation_dict)
    
    return result

# запускаем
word = input("Введите слово на латинском: ")
capitalized_word = capitalize_latin(word)
print("Преобразованное слово:", capitalized_word)

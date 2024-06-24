# В заданной строке удалить второй и четвертый по счету символы


def remove_second_and_fourth_chars(s):
    if len(s) < 4:
        raise ValueError("Строка должна содержать как минимум 4 символа.")
    
    # Удаление второго и четвертого символов
    result = s[:1] + s[2:3] + s[4:]
    return result

# Пример использования функции
input_string = input("Введите строку: ")
try:
    result_string = remove_second_and_fourth_chars(input_string)
    print(f"Результат: {result_string}")
except ValueError as e:
    print(e)

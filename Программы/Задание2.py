# Из трех данных чисел выбрать наименьшее и наибольшее.


def find_min_max(a, b, c):
    # Находим наименьшее и наибольшее числа
    min_number = min(a, b, c)
    max_number = max(a, b, c)
    
    return min_number, max_number

# Пример использования функции
a, b, c = -2, 0, 3
min_number, max_number = find_min_max(a, b, c)
print(f"Наименьшее число: {min_number}, Наибольшее число: {max_number}")

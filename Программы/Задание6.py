# Дана длина окружности. Найти площадь круга, ограниченного этой окружностью. В качестве значения Pi использовать 3.14


def find_area_of_circle(circumference):
    # Значение Пи
    pi = 3.14
    
    # Вычисление радиуса
    radius = circumference / (2 * pi)
    
    # Вычисление площади
    area = pi * radius ** 2
    
    return area

# Ввод длины окружности с клавиатуры
circumference = float(input("Введите длину окружности: "))

# Вычисление площади круга
area = find_area_of_circle(circumference)

# Вывод результата
print(f"Площадь круга, ограниченного данной окружностью: {area:.2f}")

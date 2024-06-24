# Найти периметр и площадь прямоугольного треугольника, если даны длины его катетов a и b


import math

def calculate_triangle_properties(a, b):
    # Вычисление гипотенузы
    c = math.sqrt(a**2 + b**2)
    
    # Вычисление периметра
    perimeter = a + b + c
    
    # Вычисление площади
    area = 0.5 * a * b
    
    return perimeter, area

# Ввод значений катетов с клавиатуры
a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

# Вычисление периметра и площади
perimeter, area = calculate_triangle_properties(a, b)

# Вывод результатов
print(f"Периметр треугольника: {perimeter}")
print(f"Площадь треугольника: {area}")

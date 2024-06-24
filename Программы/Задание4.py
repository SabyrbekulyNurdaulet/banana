# 1.Ввести с клавиатуры значения трех сторон треугольника a, b и c и определить, является ли он прямоугольным. Ответ вывести в виде сообщения.


def is_right_triangle(a, b, c):
    # Находим самую длинную сторону
    longest_side = max(a, b, c)
    
    # Определяем две другие стороны
    if longest_side == a:
        other_side1, other_side2 = b, c
    elif longest_side == b:
        other_side1, other_side2 = a, c
    else:
        other_side1, other_side2 = a, b
    
    # Проверяем теорему Пифагора
    if longest_side**2 == other_side1**2 + other_side2**2:
        return True
    else:
        return False

# Ввод значений сторон треугольника с клавиатуры
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

# Определение, является ли треугольник прямоугольным
if is_right_triangle(a, b, c):
    print("Треугольник является прямоугольным.")
else:
    print("Треугольник не является прямоугольным.")

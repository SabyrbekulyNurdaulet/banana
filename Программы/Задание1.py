# Даны три целых числа. Возвести в квадрат отрицательные числа и в третью степень — положительные (число 0 не изменять)


def transform_numbers(a, b, c):
    # Функция для трансформации числа в зависимости от его значения
    def transform(x):
        if x < 0:
            return x ** 2
        elif x > 0:
            return x ** 3
        else:
            return x

    # Применение функции к каждому из чисел
    a_transformed = transform(a)
    b_transformed = transform(b)
    c_transformed = transform(c)
    
    return a_transformed, b_transformed, c_transformed

# Пример использования функции
a, b, c = -2, 0, 3
result = transform_numbers(a, b, c)
print(result)  # (-2 -> 4, 0 -> 0, 3 -> 27)

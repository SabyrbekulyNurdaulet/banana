# 3. Даны натуральные числа х и у. Вычислить произведение , используя лишь операцию сложения. Задачу решить двумя способами x y

def multiply_recursively(x, y):
    if y == 0:
        return 0
    return x + multiply_recursively(x, y - 1)

# Ввод значений x и y с клавиатуры
x = int(input("Введите натуральное число x: "))
y = int(input("Введите натуральное число y: "))

# Вычисление произведения
product = multiply_recursively(x, y)

# Вывод результата
print(f"Произведение {x} и {y} равно {product}")

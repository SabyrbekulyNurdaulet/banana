def transform_string(S, N):
    current_length = len(S)
    
    if current_length > N:
        # Если длина строки S больше N, отбрасываем первые символы
        transformed_string = S[current_length - N:]
    elif current_length < N:
        # Если длина строки S меньше N, добавляем точки в начало строки
        dots_to_add = "." * (N - current_length)
        transformed_string = dots_to_add + S
    else:
        # Если длина строки S равна N, оставляем строку без изменений
        transformed_string = S
    
    return transformed_string

# Пример использования функции
S = input("Введите строку S: ")
N = int(input("Введите число N: "))

transformed_result = transform_string(S, N)
print(f"Преобразованная строка: {transformed_result}")

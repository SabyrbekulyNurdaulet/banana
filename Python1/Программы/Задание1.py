# 1. Создать программу изменения цвета

import tkinter as tk
from tkinter import ttk

# Функция для изменения цвета фона
def change_color(event):
    selected_color = color_combobox.get()
    root.config(bg=selected_color)

# Создание главного окна
root = tk.Tk()
root.title("Изменение цвета окна")
root.geometry("600x500")

# Список доступных цветов
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'white', 'black', 'grey']

# Создание и настройка выпадающего списка
color_combobox = ttk.Combobox(root, values=colors)
color_combobox.set("Выберите цвет")  # Установка начального текста
color_combobox.pack(pady=20)

# Привязка события выбора цвета к функции change_color
color_combobox.bind("<<ComboboxSelected>>", change_color)

# Запуск главного цикла программы
root.mainloop()

# import tkinter as tk
# from tkinter import ttk, colorchooser

# def choose_color():
#     chosen_color = colorchooser.askcolor(title="Выберите цвет")[1]
#     if chosen_color:
#         color_var.set(chosen_color)
#         change_color()

# def change_color(*args):
#     selected_color = color_var.get()
#     root.configure(bg=selected_color)

# root = tk.Tk()
# root.title("Изменение цвета окна")

# # Переменная для хранения выбранного цвета
# color_var = tk.StringVar(root)
# color_var.set("#ffffff")  # Задаем начальное значение

# # Кнопка для вызова диалога выбора цвета
# color_button = ttk.Button(root, text="Выбрать цвет", command=choose_color)
# color_button.grid(row=0, column=0, padx=10, pady=10)

# # Обработчик события изменения цвета
# color_var.trace("w", change_color)

# # Устанавливаем цвет окна на основе начального выбранного цвета
# change_color()

# root.mainloop()
# 7. а).Tkinter.Создать форму произвольного размера
# б).На этой форме разместить следующие элементы:
# a)Button
# b)Label
# c)Entry
# в).Каждый элемент имеет свою цветовую характеристику(фон,текст)
# г).Обработать нажатие или выбор для каждого элемента выдав
#  соответствующее сообщение.

import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "Button was clicked!")

def on_label_click(event):
    messagebox.showinfo("Label Clicked", "Label was clicked!")

def on_entry_return(event):
    messagebox.showinfo("Entry Submitted", f"Entry content: {entry.get()}")

# Создание главного окна
root = tk.Tk()
root.title("My Tkinter App")

# Установка произвольного размера формы
root.geometry("400x300")

# Создание и размещение кнопки
button = tk.Button(root, text="Click Me", bg="blue", fg="white", command=on_button_click)
button.pack(pady=20)

# Создание и размещение метки
label = tk.Label(root, text="This is a label", bg="green", fg="black")
label.pack(pady=20)
label.bind("<Button-1>", on_label_click)  # Обработка клика по метке

# Создание и размещение поля ввода
entry = tk.Entry(root, bg="yellow", fg="black")
entry.pack(pady=20)
entry.bind("<Return>", on_entry_return)  # Обработка нажатия Enter в поле ввода

# Запуск главного цикла приложения
root.mainloop()

# 18.TkinterГрафика
#Рисуем линии, прямоугольники, круг и текст в Tkinter 

import tkinter as tk

def draw_shapes():
    # Создание графического окна
    root = tk.Tk()
    root.title("Рисование фигур в Tkinter")
    
    # Создание Canvas (холста) для рисования
    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    # Рисование линии
    canvas.create_line(50, 50, 200, 50, width=2, fill='blue')

    # Рисование прямоугольника
    canvas.create_rectangle(50, 100, 150, 200, outline='red', width=2, fill='yellow')

    # Рисование круга
    canvas.create_oval(200, 100, 300, 200, outline='green', width=2, fill='lightblue')

    # Рисование текста
    canvas.create_text(100, 250, text="Пример текста", fill='purple', font=('Arial', 14))

    # Запуск главного цикла обработки событий
    root.mainloop()

# Вызов функции для отображения рисунков
draw_shapes()

# 9.TkinterГрафика Рисуем линии, прямоугольники, круг и текст в Tkinter 
 


import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Graphics")

# Создание холста (Canvas)
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Рисование линии
canvas.create_line(50, 50, 550, 50, fill="blue", width=2)

# Рисование прямоугольника
canvas.create_rectangle(100, 100, 300, 200, outline="green", width=2, fill="yellow")

# Рисование круга (окружности)
canvas.create_oval(350, 100, 500, 250, outline="red", width=2, fill="lightblue")

# Рисование текста
canvas.create_text(300, 300, text="Hello, Tkinter!", font=("Arial", 24), fill="purple")

# Запуск главного цикла приложения
root.mainloop()

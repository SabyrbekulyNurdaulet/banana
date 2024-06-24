# 3. Сделать гифку

from customtkinter import *
from tkinter.filedialog import askopenfilenames
from PIL import ImageTk, Image
 
# Создаем окно customtkinter
root = CTk()
root.geometry("800x800")
root.resizable(False, False)
 
# Подгружаем файлы с изображениями через диалоговое окно
image_paths = askopenfilenames(title='Выберите изображения для анимации',
                               filetypes=[('Image Files', '*.png *.jpg *.gif')])
 
# Создаем объекты Image из загруженных файлов
images = [Image.open(path) for path in image_paths]
 
# Получаем длительность анимации из первого изображения
duration = images[0].info.get('duration', 100)
 
# Создаем gif анимацию
images[0].save('animation.gif', save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)
 
# Загрузка GIF-файла
image = Image.open("animation.gif")
frames = []
try:
    while True:
        frames.append(image.copy())
        image.seek(len(frames))  # переход к следующему кадру
except EOFError:
    pass
 
 
# Отображение GIF-анимации
def update(frame_number):
    # Отображение кадра анимации
    frame = frames[frame_number]
    img = ImageTk.PhotoImage(frame)
    label.configure(image=img)
    label.image = img
 
    # Переход к следующему кадру
    root.after(50, update, (frame_number + 1) % len(frames))
 
 
label = CTkLabel(root, text='')
label.pack()
 
# Запуск анимации
update(0)
 
root.mainloop()








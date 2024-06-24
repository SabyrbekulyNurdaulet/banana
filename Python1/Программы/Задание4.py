import os
import shutil

def move_and_rename_file(src_path, dest_dir, new_name):
    # Проверяем, существует ли исходный файл
    if not os.path.isfile(src_path):
        print(f"Файл {src_path} не найден.")
        return

    # Проверяем, существует ли директория назначения, если нет - создаем ее
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Получаем полное имя файла назначения
    dest_path = os.path.join(dest_dir, new_name)

    # Перемещаем файл в новую директорию с новым именем
    shutil.move(src_path, dest_path)
    print(f"Файл {src_path} был перемещен в {dest_path}")

if __name__ == "__main__":
    # Запрашиваем у пользователя путь к файлу, директорию назначения и новое имя файла
    src_path = input("Введите путь к исходному файлу: ")
    dest_dir = input("Введите путь к директории назначения: ")
    new_name = input("Введите новое имя файла (с расширением): ")

    # Перемещаем и переименовываем файл
    move_and_rename_file(src_path, dest_dir, new_name)

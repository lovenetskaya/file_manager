import os
import shutil

base_dir = ''  # Введите сюда путь к рабочей директории

# Функции для работы с директориями
def make_dir(name):
    path = os.path.join(base_dir, name)
    os.mkdir(path)
    print(f"Создана директория {name} по пути {path}")

def remove_dir(name):
    path = os.path.join(base_dir, name)
    os.rmdir(path)
    print(f"Директория {name} удалена из {base_dir}")

def switch_dir(name):
    global base_dir
    if name == '..':
        base_dir = os.path.dirname(base_dir)
        print("Перешли на уровень выше")
    else:
        new_path = os.path.join(base_dir, name)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            base_dir = new_path
            print(f"Текущий путь изменен на {base_dir}")
        else:
            print(f"Директория не существует")

# Функции для работы с файлами
def create_file(name):
    path = os.path.join(base_dir, name)
    with open(path, 'w'):
        pass
    print(f"Файл {name} создан")

def write_to_file(name, text):
    path = os.path.join(base_dir, name)
    with open(path, 'w') as f:
        f.write(text)
    print(f"Текст записан в файл {name}")

def read_file(name):
    path = os.path.join(base_dir, name)
    with open(path, 'r') as f:
        content = f.read()
        print(f"Содержимое файла:\n", content)

def remove_file(name):
    path = os.path.join(base_dir, name)
    os.remove(path)
    print(f"Файл {name} удален")

# Функции для копирования и перемещения файлов
def copy_file(src, dst):
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(base_dir, dst, src)
    shutil.copyfile(src_path, dst_path)
    print(f"Файл {src} скопирован в {dst_path}")

def move_file(src, dst):
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(base_dir, dst, src)
    shutil.move(src_path, dst_path)
    print(f"Файл {src} перемещен в {dst_path}")

def rename_file(old, new):
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    os.rename(old_path, new_path)
    print(f"Файл {old} переименован в {new}")

def list_files():
    files = os.listdir(base_dir)
    for file in files:
        print(file)

choice = 0
while choice != -1:
    try:
        print('1 - Создать папку')
        print('2 - Удалить папку')
        print('3 - Сменить рабочую папку')
        print('4 - Создать файл')
        print('5 - Записать текст в файл')
        print('6 - Посмотреть содержимое файла')
        print('7 - Удалить файл')
        print('8 - Скопировать файл')
        print('9 - Переместить файл')
        print('10 - Переименовать файл')
        print('11 - Посмотреть список файлов в текущей директории')
        print('-1 - Выйти из программы\n')
        choice = int(input())
        if choice == 1:
            dir_name = str(input('Введите имя папки, которую хотите создать: '))
            make_dir(dir_name)
        elif choice == 2:
            dir_name = str(input('Введите имя папки, которую хотите удалить: '))
            remove_dir(dir_name)
        elif choice == 3:
            dir_name = str(input('Введите имя папки, в которую хотите перейти: '))
            switch_dir(dir_name)
        elif choice == 4:
            file_name = str(input('Введите имя файла, который хотите создать: '))
            create_file(file_name)
        elif choice == 5:
            file_name = str(input('Введите имя файла, в который хотите записать текст: '))
            text = str(input('Введите текст, который хотите записать в файл: '))
            write_to_file(file_name, text)
        elif choice == 6:
            file_name = str(input('Введите имя файла, который хотите прочитать: '))
            read_file(file_name)
        elif choice == 7:
            file_name = str(input('Введите имя файла, который хотите удалить: '))
            remove_file(file_name)
        elif choice == 8:
            file_name = str(input('Введите имя файла, который хотите скопировать: '))
            dir_name = str(input('Введите имя папки, в которую хотите скопировать файл: '))
            copy_file(file_name, dir_name)
        elif choice == 9:
            file_name = str(input('Введите имя файла, который хотите переместить: '))
            dir_name = str(input('Введите имя папки, в которую хотите переместить файл: '))
            move_file(file_name, dir_name)
        elif choice == 10:
            old_name = str(input('Введите старое имя файла: '))
            new_name = str(input('Введите новое имя файла: '))
            rename_file(old_name, new_name)
        elif choice == 11:
            list_files()
    except Exception as e:
        print(f"Произошла ошибка: {e}")

import os
import shutil
import configparser


def create_p(name):
    os.chdir(dir)
    os.mkdir(name)


def delete_p(name):
    if os.path.isdir(dir + name):
        os.rmdir(dir + name)


def move(name=None):
    global dir
    if name:
        os.chdir(dir + name)
        dir = dir + name + "/"
    else:
        name1 = input("Введите полный путь: ")
        os.chdir(name1)


def create_f(name, text=None):
    with open(dir + name, 'w', encoding="UTF-8") as file:
        if text:
            file.write(text)
        file.close()


def write_in_file(name, text):
    with open(dir + name, 'w', encoding="UTF-8") as f:
        f.write(text)


def see_file(name):
    f = open(dir + name)
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()


def rm_file(name):
    os.remove(dir + name)


def copy_file(name, new_name):
    shutil.copy(dir + name, dir + new_name)


def move_file(way, new_way):
    shutil.move(dir + way, dir + new_way)


def rename_file(name, new_name):
    os.rename(dir + name, dir + new_name)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("C:/Set/conf.ini")
    dir = config["Settings"]["dir"]
    ans = ("""1. Создание папки (с указанием имени);
2. Удаление папки по имени;
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
4. Создание пустых файлов с указанием имени;
5. Запись текста в файл;
6. Просмотр содержимого текстового файла;
7. Удаление файлов по имени;
8. Копирование файлов из одной папки в другую;
9. Перемещение файлов;
10. Переименование файлов.
""")
    print(ans)
    b = input().split()
    try:
        while b[0] != "exit":
            if b[0] == "1":
                i = input("Введите название папки: ")
                create_p(i)
                print(ans)
                b = input().split()
            elif b[0] == "2":
                i = input("Введите название папки: ")
                delete_p(i)
                print(ans)
                b = input().split()
            elif b[0] == "3":
                i = input("Введите название папки: ")
                move(i)
                print(ans)
                b = input().split()
            elif b[0] == "4":
                i = input("Введите название файла: ")
                create_f(i)
                print(ans)
                b = input().split()
            elif b[0] == "5":
                i = input("Введите название файла: ")
                i2 = input("Введите текст: ")
                write_in_file(i, i2)
                print(ans)
                b = input().split()
            elif b[0] == "6":
                i = input("Введите название файла: ")
                see_file(i)
                print(ans)
                b = input().split()
            elif b[0] == "7":
                i = input("Введите название файла: ")
                rm_file(i)
                print(ans)
                b = input().split()
            elif b[0] == "8":
                i = input("Введите название файла: ")
                i2 = input("Введите название нового файла: ")
                copy_file(i, i2)
                print(ans)
                b = input().split()
            elif b[0] == "9":
                i = input("Введите название первого пути: ")
                i2 = input("Введите название второго пути: ")
                move_file(b[1], b[2])
                print(ans)
                b = input().split()
            elif b[0] == "10":
                i = input("Введите название первого файла: ")
                i2 = input("Введите название новое название: ")
                rename_file(b[1], b[2])
                print(ans)
                b = input().split()
    except Exception:
        print("Что-то пошло не так!")
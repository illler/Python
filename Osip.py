# import os
# import shutil
#
# dir_name = "D:/"
#
#
# def c_file(name, text=None):
#     global dir_name
#     var = os.chdir.dir_name
#
#     with open(name, 'w', encoding='utf-8') as f:
#         if text:
#             f.write(text)
#
#             f.close()
#
#         f.close()
#
#
# def r_file(name):
#     os.remove(dir_name + name)
#
#
# def c_folder(name):
#     os.mkdir(dir_name + name)
#
#
# def r_folder(name):
#     os.rmdir(dir_name + name)
#
#
# def m_folder(name):
#     os.chdir(name)
#
#
# def w_file(name, text):
#     f = open(dir_name + name, 'a')
#
#     f.write(text)
#
#     f.close()
#
#
# def r_file(name):
#     f = open(dir_name + name)
#
#     line = f.readline()
#
#     while line:
#         print(line)
#
#         line = f.readline()
#
#         f.close()
#
#
# def c_file(name, name1):
#     shutil.copy(dir_name + name, dir_name + name1)
#
#
# def m_file(name, name1):
#     shutil.move(dir_name + name, dir_name + name1)
#
#
# def r_file(name, name1):
#     os.rename(dir_name + name, dir_name + name1)

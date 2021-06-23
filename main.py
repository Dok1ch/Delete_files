from pathlib import Path
import os, shutil
import glob

path = 'Archive/'
dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path+directory)]

#Номер папки 2019
print(dir_list)

dir2019 = []
for i in dir_list:
    if i == '2019_01' or i == '2019_02' or i == '2019_03' or i == '2019_04' or i == '2019_05' or i == '2019_06' or i == '2019_07' or i == '2019_08' or i == '2019_09' or i == '2019_10' or i == '2019_11' or i == '2019_12':
        dir2019.append(i)

path_list = []
for element in dir2019:
    path_list.append(path + element)

#Пути 'venv/Archive/2019_03'
print(path_list)

dir_list1 = []
for element in path_list:
    dir_list1.append(os.listdir(element))

#Папки дней 1, 2, 3,
print(dir_list1)

folder_paths = []
for element in path_list:
    for entry_name in os.listdir(element):
        entry_path = os.path.join(element, entry_name)
        if os.path.isdir(entry_path):
            folder_paths.append(entry_path)

#Пути 'venv/Archive/2019_03\\1'
print(folder_paths)

folder_paths1 = []
for element in folder_paths:
    for entry_name in os.listdir(element):
        entry_path = os.path.join(element, entry_name)
        if os.path.isdir(entry_path):
            folder_paths1.append(entry_path)

#Папки 'venv/Archive/2019_03\\1\\050121_о665хк11'
print(folder_paths1)

folder_paths2 = []
for element in folder_paths1:
    for entry_name in os.listdir(element):
        entry_path = os.path.join(element, entry_name)
        if os.path.isdir(entry_path):
            folder_paths2.append(entry_path)

#Путь до машины 'venv/Archive/2019_03\\1\\050121_о665хк11'
print(folder_paths2)

file_paths12 = []
file_txt = []
for element in folder_paths1:

    for file in os.listdir(element):
        if file.endswith(".txt"):
            file_txt.append(file)

    for file_name in os.listdir(element):
        file_path = os.path.join(element, file_name)

        if os.path.isfile(file_path):
            file_paths12.append(file_name)
        if file_name == 'report.jpg' or file_name.endswith(".txt"):
            file_paths12.remove(file_name)

print(file_paths12)

file_paths3 = []
for element in folder_paths1:
    for file_name in os.listdir(element):
        file_path = os.path.join(element, file_name)
        if os.path.isfile(file_path):
            file_paths3.append(file_path)

print(file_paths3)

for element in file_paths3:
    if element.endswith("report.jpg") or element.endswith(".txt"):
        print()
    else:
        os.remove(element)


#Удаление папок в авто
for element in folder_paths2:
    try:
        if os.path.isfile(element) or os.path.islink(element):
            os.unlink(element)
        elif os.path.isdir(element):
            shutil.rmtree(element)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (element, e))



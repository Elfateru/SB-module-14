import os.path

def find_file(cur_path, dirs=0, files=0, size=0):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isdir(path):
            dirs, files, size = find_file(path, dirs, files, size)
            dirs += 1
        elif os.path.isfile(path):
            files += 1
            size += os.path.getsize(path)
    return dirs, files, size




file = os.path.abspath(os.path.join('..'))
print(file)

total_dirs, total_files, file_size = find_file(file)
file_size = file_size / 1024
print('Размер каталога (в Кб):', file_size)
print('Количество подкаталогов:', total_dirs)
print('Количество файлов:', total_files)
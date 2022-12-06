import os


from collections.abc import Iterable


def gen_files_path(find_path, path=os.path.abspath(os.path.sep)) -> Iterable:
    for root, dirs, files in os.walk(path, topdown=False):
        yield root
        if root.endswith(find_path):
            break


find_dir = input('Какую директорию ищем? ')

my_gen = gen_files_path(find_dir)
for i in my_gen:
    print(i)


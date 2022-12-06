import os


def count_str(path):
    files_in_dir = os.listdir(path)
    for file in files_in_dir:
        if file.endswith('.py'):
            with open(file, 'r', encoding='utf-8') as text:
                for i_line in text:
                    if i_line.strip() and not i_line.startswith('#'):
                        yield 1


count = 0
path = os.getcwd()

counter_str = count_str(path)
for num in counter_str:
    count += num
print(count)

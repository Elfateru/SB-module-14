import zipfile


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def print_stats(stats):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    # for char, count in stats.items():
    for i_both in stats:
        print('|{: ^9}|{: ^9}|'.format(i_both[0], i_both[1]))
    print('+{:-^19}+'.format('+'))


def sort_by_frequency(stats_list):
    letters_l = []
    for sym, freq in stats_list.items():
        letters_l.append([sym, freq])
    return sorted(letters_l, key=lambda x: x[1], reverse=True)

file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)

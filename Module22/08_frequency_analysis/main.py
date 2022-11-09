def letters_filter(file):
    letters_dict = dict()
    for i_line in file:
        for i_letter in i_line.lower():
            if i_letter.isalpha():
                if i_letter not in letters_dict:
                    letters_dict[i_letter] = 0
                letters_dict[i_letter] += 1
    return letters_dict


def letters_sort(letters_dict):
    letters_l = []
    letters_total = sum(letters_dict.values())
    for sym, freq in letters_dict.items():
        freq_percent = round(freq / letters_total, 3)
        letters_l.append([sym, freq_percent])

    return sorted(letters_l, key=lambda x: (-x[1], x[0]))


def text_sort(sorted_list):
    text = ''
    for i_line in sorted_list:
        text += i_line[0] + ' ' + str(i_line[1]) + '\n'
    return text


file_from = open('text.txt', 'r')
letters_dict = letters_filter(file_from)
file_from.close()
letters_list = letters_sort(letters_dict)
text = text_sort(letters_list)

file_to = open('analysis.txt', 'w')
file_to.write(text)
file_to.close()

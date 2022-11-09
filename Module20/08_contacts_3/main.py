def add_contact(p_book):
    name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    name = tuple(name)
    if name in p_book:
        print('Такой человек уже есть в контактах.')
        return print('Текущий словарь контактов:', p_book)

    number = int(input('Введите номер телефона: '))
    p_book[name] = number
    print('Текущий словарь контактов:', p_book)


def search_contact(p_book):
    surname = input('Введите фамилию для поиска: ').lower()
    for key, val in p_book.items():
        if key[1][:-1].lower() == surname or key[1].lower() == surname or key[1].lower() == surname[:-1]:
            print(key[0], key[1], val)


phone_book = dict()

while True:
    print('Введите номер действия:\n 1. Добавить контакт\n 2. Найтичеловека')
    order = int(input())
    if order == 1:
        add_contact(phone_book)
    if order == 2:
        search_contact(phone_book)

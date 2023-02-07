import re

numbers = ['9999999999', '999999-999', '99999x9999']
pattern = r'\b[8-9]\d{9}\b'
for count, num in enumerate(numbers):
    a = re.match(pattern, num)
    if a:
        print(count + 1, 'номер: всё в порядке')
    else:
        print(count + 1, 'номер: не подходит')

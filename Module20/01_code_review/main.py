students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def hobby_and_len(new_dict):
    surname_len = 0
    hobby = set()
    for i in new_dict.values():
        hobby.update(i['interests'])
        surname_len = surname_len + len(i['surname'])
    return hobby, surname_len


id_age = [(id, age['age']) for id, age in students.items()]
print('Список пар "ID студента — возраст": ', id_age)

hobby, surname_len = hobby_and_len(students)
print('Полный список интересов всех студентов:', hobby)
print('Общая длина всех фамилий студентов:', surname_len)

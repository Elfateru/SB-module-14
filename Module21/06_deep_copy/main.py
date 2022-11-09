import pprint
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам  недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на ',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def add_site(que):
    new_site = dict()
    for _ in range(que):
        new_brand = input('Введите название продукта для нового сайта: ')

        new_site[new_brand] = copy.deepcopy(site)
        new_site[new_brand]['html']['head']['title'] = f'Куплю/продам {new_brand} недорого'
        new_site[new_brand]['html']['body']['h2'] = f'У нас самая низкая цена на {new_brand}'
        pprint.pprint(new_site)


question = int(input('Сколько будет сайтов: '))
add_site(question)

import functools
from collections.abc import Callable


def check_permission(user: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            if user in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию {func}'.format(
                    func=func.__name__
                ))

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as exc:
    print(exc)

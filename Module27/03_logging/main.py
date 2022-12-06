from typing import Callable, Any
from functools import wraps
from datetime import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор который отвечает за логирование функций
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            result = func(*args, **kwargs)
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                text = f'Ошибка в функции {func.__name__}\n' \
                       f'Дата и время ошибки {datetime.today()}\n' \
                       f'Ошибка: {exc}\n' \
                       f'------------------------------------------'
                file.write(text)
                result = 'Ошибка'
                return result
        return result
    return wrapper

@logging
def foo():
    a = 1
    return a / 0

@logging
def foo2():
    a = 1
    return v

print(foo())
print(foo2())
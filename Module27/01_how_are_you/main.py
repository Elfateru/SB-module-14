from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """Декоратор - раздражитель, не рекомендуется к использованию"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Как дела? Хорошо.\nА у меня не очень! Ладно держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapper


@how_are_you
def test():
    """Тестовая функция"""
    print('<Что тут происходит...>')

test()




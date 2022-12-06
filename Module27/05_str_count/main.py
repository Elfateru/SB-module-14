from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считаюзий и выводящий количество вызовов
    декорируемой функции.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print('Функция {func} была вызвана: {count} раз'.format(
            func=func.__name__, count=wrapper.count))
        return result
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('test')

test()
test()
test()
test()

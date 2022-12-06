import time
from typing import Callable, Any
import functools


def slowdown_func(func: Callable) -> Callable:
    """Декоратор вызывающий функцию с задержкой в три секунды"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        time.sleep(3)
        result = func(*args, **kwargs)
        return result

    return wrapper


@slowdown_func
def square_sum(number: int) -> int:
    """
        Функция нахождения суммы квадратов
        для каждого N от 0 до 10000,
        где 0 <= N <= 100

        :return: (int)сумма квадратов"""
    result = 0
    for _ in range(number):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result

print(square_sum(2))

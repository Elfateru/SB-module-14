from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор возвращаюий описание функции и заменяет её print, если возраст больше 25
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args_kwargs_list = list()
        for arg in args:
            if isinstance(arg, str):
                args_kwargs_list.append(repr(arg))
            else:
                args_kwargs_list.append(str(arg))
        for key, value in kwargs.items():
            args_kwargs_list.append(repr(f'{key}={value}'))
        args_kwargs_str = ', '.join(args_kwargs_list)
        print('\nВызывается функция {func}({a})'.format(func=func.__name__, a=args_kwargs_str))
        print('{func} вернула значение {meaning}'.format(func=repr(func.__name__), meaning=repr(func(*args, **kwargs))))
        if kwargs:
            for i_elem in kwargs.values():
                if isinstance(i_elem, int):
                    if i_elem > 25:
                        return print(f'Ого, {arg}! Тебе уже {i_elem} лет, ты вырос!')
        return print(func(*args, **kwargs))

    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

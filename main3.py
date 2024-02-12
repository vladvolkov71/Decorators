import os
from functools import wraps
from datetime import datetime


def logger(p):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            # действия до вызова исходной функции

            s = f"{datetime.now()}. Вызывается функция {old_function.__name__} с аргументами {args} и {kwargs}.\n"

            result = old_function(*args, **kwargs)
            # действия после вызова исходной функции
            s1 = f"Функция вернула результат {result}.\n"
            with open(p, 'a', encoding='utf-8', newline='\n') as f:
                f.write(s)
                f.write(s1)

            return result

        return new_function

    return __logger


def test(p1):
    path = p1
    if os.path.exists(path):
        os.remove(path)

    nested_list = [
        ['a', 'b', [1, [4, 5, 6], 2, 3], 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    @logger(path)
    def recursive_flatten_generator(arr):
        for i in arr:
            if isinstance(i, list):
                yield from recursive_flatten_generator(i)
            else:
                yield i

    flat_list = [item for item in recursive_flatten_generator(nested_list)]
    print(*flat_list)


if __name__ == '__main__':
    test('log_4.log')

from timeit import default_timer as timer
from typing import Callable

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num: int) -> Callable:
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func: Callable):
        # put your code here
        def repeater(*args, **kwargs):
            start_time = timer()
            for _ in range(num):
                start_iter_time = timer()
                func(*args, **kwargs)
                end_iter_time = timer()
                print(end_iter_time - start_iter_time)
            end_time = timer()
            print((end_time - start_time) / num)

        return repeater

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

# Standard Library
from contextlib import contextmanager
from functools import wraps


def timeit(func):
    import time

    def wrapped(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time() - begin
        print(f"{func.__name__} spent {round(end * 1000, 5)} µs")
        return res

    return wrapped


@timeit
def mapper():
    map(lambda x: x ** 2, [i for i in range(100)])


def timeit_2(func):
    import time

    @wraps(func)
    def wrapped(min_secs, *args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time() - begin
        if end > min_secs:
            print(f"{func.__name__} spent {round(end * 1000, 5)} µs")
        return res

    return wrapped


@timeit_2
def mapper_2():
    """Square list of range 100."""
    map(lambda x: x ** 2, [i for i in range(100)])


@contextmanager
def timeit_3(min_secs):
    import time

    begin = time.time()
    try:
        yield
    finally:
        end = time.time() - begin
        if end > min_secs:
            print(f"Spent {round(end * 1000, 5)} µs")


def mapper_3():
    """Square list of range 100."""
    map(lambda x: x ** 2, [i for i in range(100)])


if __name__ == "__main__":
    print("Decorator 1:")
    mapper()

    print("Decorator 2:")
    print(mapper_2.__doc__)
    mapper_2(1.4e-8)

    print("Decorator 3:")
    with timeit_3(1.4e-8):
        mapper_3()

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


if __name__ == "__main__":
    @timeit
    def mapper():
        map(lambda x: x ** 2, [i for i in range(1_000_000)])

    print("Decorator 1:")
    mapper()

    @timeit_2
    def mapper_2():
        """Square list of range 1_000_000."""
        map(lambda x: x ** 2, [i for i in range(1_000_000)])

    print("Decorator 2:")
    print(mapper_2.__doc__)
    mapper_2(1.4e-8)

    def mapper_3():
        """Square list of range 1000000."""
        map(lambda x: x ** 2, [i for i in range(1_000_000)])

    print("Decorator 3:")
    with timeit_3(1.4e-8):
        mapper_3()

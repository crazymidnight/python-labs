class FibonacciIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.previous = 0
        self.current = 1

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            # flake8 ignore
            self.previous, self.current = self.current, self.previous + self.current
            return self.previous
        else:
            raise StopIteration


class GeometricIterator:
    def __iter__(self):
        return self

    def __init__(self, limit, ratio):
        self.limit = limit
        self.counter = 0
        self.previous = 1
        self.current = 1
        self.ratio = ratio

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.previous, self.current = self.current, self.current * self.ratio
            return self.previous
        else:
            raise StopIteration


class CountdownIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit + 1
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.limit - self.counter
        else:
            raise StopIteration


if __name__ == "__main__":
    print("Fibonacci iterator:")
    fib = FibonacciIterator(limit=10)
    for i in fib:
        print(i)

    print("Geometric Iterator:")
    geom = GeometricIterator(limit=10, ratio=2)
    for i in geom:
        print(i)

    print("Countdown Iterator:")
    count = CountdownIterator(limit=100)
    for i in count:
        print(i)

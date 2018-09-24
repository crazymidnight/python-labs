def fibonacci(numbers):
    previous = 0
    current = 1
    for _ in range(numbers):
        yield current
        previous, current = current, previous + current


def geometric(start, numbers, ratio):
    for _ in range(numbers):
        yield start
        start *= ratio


def countdown(n):
    for i in range(n + 1):
        yield n - i


if __name__ == "__main__":
    print("Fibonacci:")
    for i in fibonacci(10):
        print(i)

    print("Geometric:")
    for i in geometric(1, 15, 2):
        print(i)

    print("Countdown:")
    for i in countdown(100):
        print(i)

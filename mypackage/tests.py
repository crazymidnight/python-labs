import contextlib
import types
import unittest

import decorators
import generators
import iterators


class TestFibonacciGenerator(unittest.TestCase):
    """Test case for Fibonacci generator."""

    def test_length(self):
        """Test Fibonacci sequence length."""
        fibonacci = list(generators.fibonacci(10))
        self.assertEqual(len(fibonacci), 10)

    def test_type(self):
        """Test type of Fibonacci sequence element."""
        fibonacci = [x for x in generators.fibonacci(10)]
        self.assertEqual(type(fibonacci[0]), int)

    def test_fibonacci(self):
        """Test sign of Fibonacci sequence elements."""
        fibonacci = [x for x in generators.fibonacci(10)]
        self.assertEqual(fibonacci[7], 21)


class TestGeometricGenerator(unittest.TestCase):
    """Test case for Geometric generator."""

    def test_length(self):
        """Test geometric sequence length."""
        geometric = [x for x in generators.geometric(0, 10, 2)]
        self.assertEqual(len(geometric), 10)

    def test_type(self):
        """Test type of geometric sequence element."""
        geometric = [x for x in generators.geometric(1, 10, 0.5)]
        type_of_geometric = type(geometric[0])
        self.assertTrue(type_of_geometric == int or type_of_geometric == float)


class TestCountdownGenerator(unittest.TestCase):
    """Test case for countdown generator."""

    def test_length(self):
        """Test countdown sequence length."""
        countdown = [x for x in generators.countdown(10)]
        self.assertEqual(len(countdown), 11)

    def test_type(self):
        """Test type of countdown sequence element."""
        countdown = [x for x in generators.countdown(10)]
        type_of_countdown = type(countdown[0])
        self.assertTrue(type_of_countdown == int or type_of_countdown == float)

    def test_last_is_zero(self):
        """Test countdown last element is zero."""
        countdown = [x for x in generators.countdown(10)]
        self.assertEqual(countdown[::-1][0], 0)


class TestFibonacciIterator(unittest.TestCase):
    """Test case for Fibonacci iterator."""

    def test_length(self):
        """Test Fibonacci sequence length."""
        fibonacci = [x for x in iterators.FibonacciIterator(10)]
        self.assertEqual(len(fibonacci), 10)

    def test_type(self):
        """Test type of Fibonacci sequence element."""
        fibonacci = [x for x in iterators.FibonacciIterator(10)]
        self.assertEqual(type(fibonacci[0]), int)

    def test_fibonacci(self):
        """Test sign of Fibonacci sequence elements."""
        fibonacci = [x for x in iterators.FibonacciIterator(10)]
        self.assertEqual(fibonacci[7], 21)


class TestGeometricIterator(unittest.TestCase):
    """Test case for Geometric iterator."""

    def test_length(self):
        """Test geometric sequence length."""
        geometric = [x for x in iterators.GeometricIterator(limit=10, ratio=2)]
        self.assertEqual(len(geometric), 10)

    def test_type(self):
        """Test type of geometric sequence element."""
        geometric = [x for x in iterators.GeometricIterator(limit=10, ratio=0.5)]
        type_of_geometric = type(geometric[0])
        self.assertTrue(type_of_geometric == int or type_of_geometric == float)


class TestCountdownIterator(unittest.TestCase):
    """Test case for countdown iterator."""

    def test_length(self):
        """Test countdown sequence length."""
        countdown = [x for x in iterators.CountdownIterator(10)]
        self.assertEqual(len(countdown), 11)

    def test_type(self):
        """Test type of countdown sequence element."""
        countdown = [x for x in iterators.CountdownIterator(10)]
        type_of_countdown = type(countdown[0])
        self.assertTrue(type_of_countdown == int or type_of_countdown == float)

    def test_last_is_zero(self):
        """Test countdown last element is zero."""
        countdown = [x for x in iterators.CountdownIterator(10)]
        self.assertEqual(countdown[::-1][0], 0)


class TestDecorator(unittest.TestCase):
    """Test case for timeit decorator."""

    def test_func(self):
        """Test decorator 1 returns function."""
        def func():
            return 0
        self.assertEqual(type(decorators.timeit(func)), types.FunctionType)

    def test_func_2(self):
        """Test decorator 2 returns function."""
        def func():
            return 0
        self.assertEqual(type(decorators.timeit_2(func)), types.FunctionType)

    def test_context(self):
        """Test decorator 3 returns contextmanager."""
        def func():
            return 0
        self.assertEqual(type(decorators.timeit_3(func)), contextlib._GeneratorContextManager)


if __name__ == "__main__":
    unittest.main()

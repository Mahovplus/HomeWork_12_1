
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_other = Runner("Произвольное имя")
        test_call = [test_other.walk() for _ in  range(10)]
        self.assertEqual(test_other.distance, 50)

    def test_run(self):
        test_other = Runner("Произвольное имя")
        test_call = [test_other.run() for _ in range(10)]
        self.assertEqual(test_other.distance, 100)

    def test_challenge(self):
        object = Runner('Continue')
        other_object = Runner('Return')
        call_func_walk = [object.walk() for _ in  range(10)]
        call_func_run = [other_object.run() for _ in range(10)]
        self.assertNotEqual(object.distance, other_object.distance)

if __name__ == '__main__':
    unittest.main()
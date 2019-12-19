import unittest

from aoc2019.src.common.utils import get_path
from aoc2019.src.day18.solution import part_one


class TestDay18(unittest.TestCase):

    def test_shortest_path_test1(self):
        self.assertEqual(part_one(get_path(__file__, 'test1.txt')), 8)

    def test_shortest_path_test2(self):
        self.assertEqual(part_one(get_path(__file__, 'test2.txt')), 86)


if __name__ == '__main__':
    unittest.main()

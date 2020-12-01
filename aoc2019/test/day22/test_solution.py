# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from common.file_utils import get_path, read_lines
from aoc2019.src.day22.solution import part_one, Shuffler


class TestDay22(unittest.TestCase):
    @staticmethod
    def to_int_list(cards: str):
        return list(map(int, cards.split(' ')))

    def test_deal_into_new_stack(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('9 8 7 6 5 4 3 2 1 0'), shuffler.deal_into_new_stack())

    def test_deal_with_increment(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('0 7 4 1 8 5 2 9 6 3'), shuffler.deal_with_increment(3))

    def test_cut_positive(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('3 4 5 6 7 8 9 0 1 2'), shuffler.cut(3))

    def test_cut_negative(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('6 7 8 9 0 1 2 3 4 5'), shuffler.cut(-4))

    def test_case1(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('0 3 6 9 2 5 8 1 4 7'),
                         shuffler.apply_techniques(read_lines(get_path(__file__, 'test1.txt'))))

    def test_case2(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('3 0 7 4 1 8 5 2 9 6'),
                         shuffler.apply_techniques(read_lines(get_path(__file__, 'test2.txt'))))

    def test_case3(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('6 3 0 7 4 1 8 5 2 9'),
                         shuffler.apply_techniques(read_lines(get_path(__file__, 'test3.txt'))))

    def test_case4(self):
        shuffler = Shuffler(10)
        self.assertEqual(self.to_int_list('9 2 5 8 1 4 7 0 3 6'),
                         shuffler.apply_techniques(read_lines(get_path(__file__, 'test4.txt'))))

    def test_part_one(self):
        self.assertEqual(8326, part_one(get_path(__file__, 'input.txt'), 10007, 2019))


if __name__ == '__main__':
    unittest.main()

# Copyright 2021 Google LLC
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

from aoc2021.src.day04.solution import BingoBoard, part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(__file__, *args, **kwargs)

    def test_board_with_row_wins(self):
        board = BingoBoard(numbers=(
            (14, 21, 17, 24, 4),
            (10, 16, 15, 9, 19),
            (18, 8, 23, 26, 20),
            (22, 11, 13, 6, 5),
            (2, 0, 12, 3, 7)
        ))
        self.assertFalse(board.mark(drawing_number=14))
        self.assertFalse(board.mark(drawing_number=21))
        self.assertFalse(board.mark(drawing_number=17))
        self.assertFalse(board.mark(drawing_number=24))
        self.assertTrue(board.mark(drawing_number=4))
        # Sum of all rows except first one.
        self.assertEqual(245, board.sum_unmarked())

    def test_board_with_column_wins(self):
        board = BingoBoard(numbers=(
            (14, 21, 17, 24, 4),
            (10, 16, 15, 9, 19),
            (18, 8, 23, 26, 20),
            (22, 11, 13, 6, 5),
            (2, 0, 12, 3, 7)
        ))
        self.assertFalse(board.mark(drawing_number=14))
        self.assertFalse(board.mark(drawing_number=10))
        self.assertFalse(board.mark(drawing_number=18))
        self.assertFalse(board.mark(drawing_number=22))
        self.assertTrue(board.mark(drawing_number=2))
        # Sum of all columns except first one.
        self.assertEqual(259, board.sum_unmarked())

    def test_part_one_with_example(self):
        self.assertEqual(4512, part_one(bingo=self.examples[0]))

    def test_part_one_with_input(self):
        self.assertEqual(87456, part_one(bingo=self.input))

    def test_part_two_with_example(self):
        self.assertEqual(1924, part_two(bingo=self.examples[0]))

    def test_part_two_with_input(self):
        self.assertEqual(15561, part_two(bingo=self.input))


if __name__ == '__main__':
    unittest.main()

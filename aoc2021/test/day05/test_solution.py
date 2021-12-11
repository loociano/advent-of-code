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

from aoc2021.src.day05.solution import Grid, part_one
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(__file__, *args, **kwargs)

    def test_grid_with_no_overlap_points(self):
        grid = Grid(width=5)
        grid.populate_vertical(y_start=0, y_end=4, x=0)
        self.assertEqual(0, grid.count_overlap_points())

    def test_grid_with_one_overlap_point(self):
        grid = Grid(width=9)
        grid.populate_vertical(y_start=1, y_end=2, x=2)
        grid.populate_horizontal(x_start=0, x_end=8, y=1)
        self.assertEqual(1, grid.count_overlap_points())

    def test_part_one_with_example(self):
        self.assertEqual(5, part_one(segment_lines=self.examples[0]))

    def test_part_one_with_input(self):
        self.assertEqual(7436, part_one(segment_lines=self.input))


if __name__ == '__main__':
    unittest.main()

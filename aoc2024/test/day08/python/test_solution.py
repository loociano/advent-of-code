# Copyright 2024 Google LLC
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

from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase
from aoc2024.src.day08.python.solution import count_antinodes


class TestDay08Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestDay08Solution, self).__init__(__file__, *args, **kwargs))

  def test_part1_withExample_counts(self):
    self.assertEqual(14, count_antinodes(self.examples[0]))

  def test_part1_withPuzzleInput_counts(self):
    self.assertEqual(327, count_antinodes(self.input))

  def test_part2_withExample_counts(self):
    self.assertEqual(34, count_antinodes(self.examples[0], any_grid_position=True))

  def test_part2_withPuzzleInput_counts(self):
    self.assertEqual(1233, count_antinodes(self.input, any_grid_position=True))


if __name__ == '__main__':
  unittest.main()

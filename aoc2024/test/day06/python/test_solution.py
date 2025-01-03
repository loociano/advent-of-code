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

from aoc2024.src.day06.python.solution import count_distinct_positions, count_positions_with_loop
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part1_withExample_counts(self):
    self.assertEqual(41, count_distinct_positions(self.examples[0]))

  def test_part1_withPuzzleInput_counts(self):
    self.assertEqual(5564, count_distinct_positions(self.input))

  def test_part2_withExample_countsPositionsWithLoop(self):
    self.assertEqual(6, count_positions_with_loop(self.examples[0]))

  def test_part2_withPuzzleInput_countsPositionsWithLoop(self):
    self.assertEqual(1976, count_positions_with_loop(self.input))


if __name__ == '__main__':
  unittest.main()

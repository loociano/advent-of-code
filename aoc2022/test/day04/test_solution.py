# Copyright 2022 Google LLC
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

from aoc2022.src.day04.solution import count_fully_contained_pairs, count_overlapping_pairs
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay04Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay04Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsPriorities(self):
    self.assertEqual(2, count_fully_contained_pairs(self.examples[0]))

  def test_part1_withPuzzleInput_returnsPriorities(self):
    self.assertEqual(509, count_fully_contained_pairs(self.input))

  def test_part2_withExampleInput_returnsPriorities(self):
    self.assertEqual(4, count_overlapping_pairs(self.examples[0]))

  def test_part2_withPuzzleInput_returnsPriorities(self):
    self.assertEqual(870, count_overlapping_pairs(self.input))


if __name__ == '__main__':
  unittest.main()

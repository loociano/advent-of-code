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

from aoc2022.src.day14.python.solution import count_resting_sand_units
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay14Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay14Solution, self).__init__(__file__, *args, **kwargs)

  def test_simulateSandFall_withExample_correctCount(self):
    self.assertEqual(24, count_resting_sand_units(self.examples[0]))

  def test_simulateSandFall_withPuzzleExample_correctCount(self):
    self.assertEqual(843, count_resting_sand_units(self.input))

  def test_simulateSandFall_withExampleAndInfiniteFloor_correctCount(self):
    self.assertEqual(93, count_resting_sand_units(self.examples[0],
                                                  infinite_floor=True))

  def test_simulateSandFall_withPuzzleInputAndInfiniteFloor_correctCount(self):
    self.assertEqual(27625, count_resting_sand_units(self.input,
                                                  infinite_floor=True))


if __name__ == '__main__':
  unittest.main()

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

from aoc2022.src.day01.python.solution import find_max_calories, find_top3_max_calories
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay01Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay01Solution, self).__init__(__file__, *args, **kwargs)


  def test_part1_withExampleInput_findsMaximumCalories(self):
    self.assertEqual(24000, find_max_calories(self.examples[0]))


  def test_part1_withPuzzleInput_findsMaximumCalories(self):
    self.assertEqual(69528, find_max_calories(self.input))


  def test_part2_withExampleInput_findsTop3MaximumCalories(self):
    self.assertEqual(45000, find_top3_max_calories(self.examples[0]))


  def test_part2_withPuzzleInput_findsTop3MaximumCalories(self):
    self.assertEqual(206152, find_top3_max_calories(self.input))


if __name__ == '__main__':
  unittest.main()

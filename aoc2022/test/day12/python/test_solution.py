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

from aoc2022.src.day12.python.solution import min_steps_to_top
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay12Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay12Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsMinSteps(self):
    self.assertEqual(31, min_steps_to_top(self.examples[0]))

  def test_part1_withPuzzleInput_returnsMinSteps(self):
    self.assertEqual(462, min_steps_to_top(self.input))

  def test_part2_withExampleInput_returnsMinSteps(self):
    self.assertEqual(29, min_steps_to_top(self.examples[0], start_char='a'))

  def test_part2_withPuzzleInput_returnsMinSteps(self):
    self.assertEqual(451, min_steps_to_top(self.input, start_char='a'))


if __name__ == '__main__':
  unittest.main()

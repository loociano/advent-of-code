# Copyright 2025 Google LLC
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
from parameterized import parameterized

from aoc2025.src.day03.python.solution import find_max_joltage, calc_total_output_joltage
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class JoltageTest(unittest.TestCase):
  @parameterized.expand([
    ('987654321111111', 98),
    ('811111111111119', 89),
    ('234234234234278', 78),
    ('818181911112111', 92),
  ])
  def testFindMaxJoltage_success(self, bank, expected):
    self.assertEqual(expected, find_max_joltage(bank))


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def testCalcTotalOutputJoltage_withSampleInput(self):
    self.assertEqual(357, calc_total_output_joltage(banks=self.examples[0]))

  def testCalcTotalOutputJoltage_withPuzzleInput(self):
    self.assertEqual(17158, calc_total_output_joltage(banks=self.input))


if __name__ == '__main__':
  unittest.main()

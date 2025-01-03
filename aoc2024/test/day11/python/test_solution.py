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
from aoc2024.src.day11.python.solution import count_stones


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, read_raw=True, *args, **kwargs)

  def test_part1_withOneBlink_counts(self):
    self.assertEqual(7, count_stones(initial_state='0 1 10 99 999', blinks=1))

  def test_part1_with3Blinks_counts(self):
    self.assertEqual(5, count_stones(initial_state='125 17', blinks=3))

  def test_part1_withMoreBlinks_counts(self):
    self.assertEqual(22, count_stones(initial_state='125 17', blinks=6))

  def test_part1_withEvenMoreBlinks_counts(self):
    self.assertEqual(55312, count_stones(initial_state='125 17', blinks=25))

  def test_part1_withPuzzleInput_counts(self):
    self.assertEqual(203457, count_stones(
      initial_state=self.input,
      blinks=25))

  def test_part2_withPuzzleInput_counts(self):
    self.assertEqual(241394363462435, count_stones(
      initial_state=self.input,
      blinks=75))


if __name__ == '__main__':
  unittest.main()

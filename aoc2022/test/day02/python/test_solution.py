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

from aoc2022.src.day02.python.solution import get_score, get_score2
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay02Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay02Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_getsScore(self):
    self.assertEqual(15, get_score(self.examples[0]))

  def test_part1_withPuzzleInput_getsScore(self):
    self.assertEqual(11603, get_score(self.input))

  def test_part2_withExampleInput_getsScore(self):
    self.assertEqual(12, get_score2(self.examples[0]))

  def test_part2_withPuzzleInput_getsScore(self):
    self.assertEqual(12725, get_score2(self.input))


if __name__ == '__main__':
  unittest.main()

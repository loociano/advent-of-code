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
from aoc2024.src.day10.python.solution import get_score_sum, get_rating_sum


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part1_withExample_getsScore(self):
    self.assertEqual(2, get_score_sum(self.examples[0]))

  def test_part1_withExample2_getsScore(self):
    self.assertEqual(4, get_score_sum(self.examples[1]))

  def test_part1_withExample3_getsScore(self):
    self.assertEqual(3, get_score_sum(self.examples[2]))

  def test_part1_withExample4_getsScore(self):
    self.assertEqual(36, get_score_sum(self.examples[3]))

  def test_part1_withPuzzleInput_getsScore(self):
    self.assertEqual(825, get_score_sum(self.input))

  def test_part2_withExample_getsRating(self):
    self.assertEqual(3, get_rating_sum(self.examples[4]))

  def test_part2_withExample2_getsRating(self):
    self.assertEqual(13, get_rating_sum(self.examples[5]))

  def test_part2_withExample3_getsRating(self):
    self.assertEqual(227, get_rating_sum(self.examples[6]))

  def test_part2_withExample4_getsRating(self):
    self.assertEqual(81, get_rating_sum(self.examples[7]))

  def test_part2_withPuzzleInput_getsRating(self):
    self.assertEqual(1805, get_rating_sum(self.input))


if __name__ == '__main__':
  unittest.main()

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
from aoc2024.src.day13.python.solution import min_tokens_to_win


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_correct(self):
    self.assertEqual(280, min_tokens_to_win(self.examples[0]))

  def test_part1_withExample2_correct(self):
    self.assertIsNone(min_tokens_to_win(self.examples[1]))

  def test_part1_withExample3_correct(self):
    self.assertEqual(200, min_tokens_to_win(self.examples[2]))

  def test_part1_withExample4_correct(self):
    self.assertIsNone(min_tokens_to_win(self.examples[3]))

  def test_part1_withExample5_correct(self):
    self.assertEqual(480, min_tokens_to_win(self.examples[4]))

  def test_part1_withPuzzleInput_correct(self):
    self.assertEqual(32067, min_tokens_to_win(self.input))

  def test_part2_withPuzzleInput_correct(self):
    self.assertEqual(92871736253789, min_tokens_to_win(self.input, price_offset=10000000000000))


if __name__ == '__main__':
  unittest.main()

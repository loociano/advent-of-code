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
from aoc2024.src.day19.python.solution import num_possible_designs, num_possible_options


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_success(self):
    self.assertEqual(6, num_possible_designs(self.examples[0]))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual(365, num_possible_designs(self.input))

  def test_part2_withExample_success(self):
    self.assertEqual(16, num_possible_options(self.examples[0]))

  def test_part2_withPuzzleInput_success(self):
    self.assertEqual(730121486795169, num_possible_options(self.input))


if __name__ == '__main__':
  unittest.main()

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
from aoc2024.src.day21.python.solution import get_complexity, get_total_complexity


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_doorCodeComplexity_withExample_success(self):
    self.assertEqual(68 * 29, get_complexity('029A'))

  def test_totalComplexity_withExample_success(self):
    self.assertEqual(126384, get_total_complexity(self.examples[0]))

  def test_totalComplexity_withPuzzleInput_success(self):
    self.assertEqual(177814, get_total_complexity(self.input))

  def test_totalComplexity_withMoreRobots_withInput_success(self):
    self.assertEqual(220493992841852, get_total_complexity(self.input, num_dir_keypads=25))


if __name__ == '__main__':
  unittest.main()

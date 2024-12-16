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
from aoc2024.src.day16.python.solution import get_min_score


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_correct(self):
    self.assertEqual(7036, get_min_score(self.examples[0]))

  def test_part1_withSecondExample_correct(self):
    self.assertEqual(11048, get_min_score(self.examples[1]))

  def test_part1_withPuzzleInput_correct(self):
    self.assertEqual(107512, get_min_score(self.input))


if __name__ == '__main__':
  unittest.main()

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
from aoc2024.src.day20.python.solution import count_cheats


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_success(self):
    self.assertEqual(1, count_cheats(self.examples[0], min_picosec_savings=64))
    self.assertEqual(2, count_cheats(self.examples[0], min_picosec_savings=40))
    self.assertEqual(3, count_cheats(self.examples[0], min_picosec_savings=38))
    self.assertEqual(4, count_cheats(self.examples[0], min_picosec_savings=36))
    self.assertEqual(5, count_cheats(self.examples[0], min_picosec_savings=20))
    self.assertEqual(44, count_cheats(self.examples[0], min_picosec_savings=0))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual(1448, count_cheats(self.input, min_picosec_savings=100))


if __name__ == '__main__':
  unittest.main()

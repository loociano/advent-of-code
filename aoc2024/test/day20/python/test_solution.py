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
    self.assertEqual(8, count_cheats(self.examples[0], min_picosec_savings=12))
    self.assertEqual(10, count_cheats(self.examples[0], min_picosec_savings=10))
    self.assertEqual(14, count_cheats(self.examples[0], min_picosec_savings=8))
    self.assertEqual(16, count_cheats(self.examples[0], min_picosec_savings=6))
    self.assertEqual(30, count_cheats(self.examples[0], min_picosec_savings=4))
    self.assertEqual(44, count_cheats(self.examples[0], min_picosec_savings=2))
    self.assertEqual(44, count_cheats(self.examples[0], min_picosec_savings=0))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual(1448, count_cheats(self.input, min_picosec_savings=100))

  def test_part2_withExample_success(self):
    self.assertEqual(3, count_cheats(self.examples[0],
                                     min_picosec_savings=76,
                                     max_cheat_length=20))
    self.assertEqual(7, count_cheats(self.examples[0],
                                     min_picosec_savings=74,
                                     max_cheat_length=20))
    self.assertEqual(29, count_cheats(self.examples[0],
                                      min_picosec_savings=72,
                                      max_cheat_length=20))

  def test_part2_withPuzzleInput_success(self):
    # 233268 too low.
    self.assertEqual(1017615, count_cheats(self.input,
                                           min_picosec_savings=100,
                                           max_cheat_length=20))


if __name__ == '__main__':
  unittest.main()

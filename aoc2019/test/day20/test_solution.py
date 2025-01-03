# Copyright 2019 Google LLC
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
from aoc2019.src.day20.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__,*args, **kwargs)

  def test_case1(self):
    self.assertEqual(23, part_one(self.examples[0]))

  def test_case2(self):
    self.assertEqual(58, part_one(self.examples[1]))

  def test_puzzle_input(self):
    self.assertEqual(514, part_one(self.input))

  def test_case1_recursive_spaces(self):
    self.assertEqual(26, part_two(self.examples[0]))

  def test_case3_recursive_spaces(self):
    self.assertEqual(396, part_two(self.examples[2]))

  def test_case3_puzzle_input(self):
    self.assertEqual(6208, part_two(self.input))


if __name__ == '__main__':
  unittest.main()

# Copyright 2020 Google LLC
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

from aoc2020.test.common.AdventOfCodeTestCase import AdventOfCodeTestCase
from aoc2020.src.day15.solution import part_one


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example1(self):
    self.assertEqual(436, part_one(starting_numbers=[0, 3, 6]))

  def test_part_one_with_example2(self):
    self.assertEqual(1, part_one(starting_numbers=[1, 3, 2]))

  def test_part_one_with_example3(self):
    self.assertEqual(10, part_one(starting_numbers=[2, 1, 3]))

  def test_part_one_with_example4(self):
    self.assertEqual(27, part_one(starting_numbers=[1, 2, 3]))

  def test_part_one_with_example5(self):
    self.assertEqual(78, part_one(starting_numbers=[2, 3, 1]))

  def test_part_one_with_example6(self):
    self.assertEqual(438, part_one(starting_numbers=[3, 2, 1]))

  def test_part_one_with_example7(self):
    self.assertEqual(1836, part_one(starting_numbers=[3, 1, 2]))

  def test_part_one_with_input(self):
    self.assertEqual(639, part_one(
        starting_numbers=[int(i) for i in self.input[0].split(',')]))

if __name__ == '__main__':
  unittest.main()

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

from aoc2020.src.day18.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example1(self):
    self.assertEqual(71, part_one(['1 + 2 * 3 + 4 * 5 + 6']))

  def test_part_one_with_example2(self):
    self.assertEqual(51, part_one(['1 + (2 * 3) + (4 * (5 + 6))']))

  def test_part_one_with_example3(self):
    self.assertEqual(26, part_one(['2 * 3 + (4 * 5)']))

  def test_part_one_with_example4(self):
    self.assertEqual(437, part_one(['5 + (8 * 3 + 9 + 3 * 4 * 3)']))

  def test_part_one_with_example5(self):
    self.assertEqual(
        12240, part_one(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']))

  def test_part_one_with_example6(self):
    self.assertEqual(
        13632, part_one(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']))

  def test_part_one_with_input(self):
    self.assertEqual(8929569623593, part_one(self.input))

  def test_part_two_with_example1(self):
    self.assertEqual(231, part_two(['1 + 2 * 3 + 4 * 5 + 6']))

  def test_part_two_with_example2(self):
    self.assertEqual(51, part_two(['1 + (2 * 3) + (4 * (5 + 6))']))

  def test_part_two_with_example3(self):
    self.assertEqual(46, part_two(['2 * 3 + (4 * 5)']))

  def test_part_two_with_example4(self):
    self.assertEqual(1445, part_two(['5 + (8 * 3 + 9 + 3 * 4 * 3)']))

  def test_part_two_with_example5(self):
    self.assertEqual(669060,
                     part_two(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']))

  def test_part_two_with_example6(self):
    self.assertEqual(
        23340, part_two(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']))

  def test_part_two_with_input(self):
    self.assertEqual(231235959382961, part_two(self.input))

if __name__ == '__main__':
  unittest.main()

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

from aoc2020.src.day07.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example(self):
    self.assertEqual(
        4, part_one(rules=self.examples[0], target_color='shiny gold'))

  def test_part_one_with_input(self):
    self.assertEqual(
        238, part_one(rules=self.input, target_color='shiny gold'))

  def test_part_two_with_example1(self):
    self.assertEqual(
        32, part_two(rules=self.examples[0], target_color='shiny gold'))

  def test_part_two_with_example2(self):
    self.assertEqual(
        126, part_two(rules=self.examples[1], target_color='shiny gold'))

  def test_part_two_with_input(self):
    self.assertEqual(
        82930, part_two(rules=self.input, target_color='shiny gold'))

if __name__ == '__main__':
  unittest.main()

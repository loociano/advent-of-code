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

from aoc2020.src.day04.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example(self):
    self.assertEqual(2, part_one(batch_file=self.examples[0]))

  def test_part_one_with_input(self):
    self.assertEqual(260, part_one(batch_file=self.input))

  def test_part_two_with_invalid_passports(self):
    self.assertEqual(0, part_two(batch_file=self.examples[1]))

  def test_part_two_with_valid_passports(self):
    self.assertEqual(4, part_two(batch_file=self.examples[2]))

  def test_part_two_with_input(self):
    self.assertEqual(153, part_two(batch_file=self.input))


if __name__ == '__main__':
  unittest.main()

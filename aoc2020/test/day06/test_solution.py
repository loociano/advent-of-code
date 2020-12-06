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
from aoc2020.src.day06.solution import part_one, part_two


class TestDay06(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay06, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_examples(self):
    self.assertEqual(6, part_one(group_answers=self.examples[0]))
    self.assertEqual(11, part_one(group_answers=self.examples[1]))

  def test_part_one_with_input(self):
    self.assertEqual(6259, part_one(group_answers=self.input))

  def test_part_two_with_examples(self):
    self.assertEqual(3, part_two(group_answers=self.examples[0]))
    self.assertEqual(6, part_two(group_answers=self.examples[1]))

  def test_part_two_with_input(self):
    self.assertEqual(3178, part_two(group_answers=self.input))

if __name__ == '__main__':
  unittest.main()

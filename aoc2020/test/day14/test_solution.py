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
from aoc2020.src.day14.solution import apply_mask, part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_apply_mask1(self):
    self.assertEqual(73, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=11))

  def test_apply_mask2(self):
    self.assertEqual(101, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=101))

  def test_apply_mask3(self):
    self.assertEqual(64, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=0))

  def test_part_one_with_example(self):
    self.assertEqual(165, part_one(program=self.examples[0]))

  def test_part_one_with_input(self):
    self.assertEqual(11327140210986, part_one(program=self.input))


if __name__ == '__main__':
  unittest.main()

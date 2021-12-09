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

from aoc2020.src.day14.solution \
    import apply_mask, apply_mask2, calculate_addresses, part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_apply_mask_example1(self):
    self.assertEqual(73, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=11))

  def test_apply_mask_example2(self):
    self.assertEqual(101, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=101))

  def test_apply_mask_example3(self):
    self.assertEqual(64, apply_mask(
        mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', value=0))

  def test_part_one_with_example(self):
    self.assertEqual(165, part_one(program=self.examples[0]))

  def test_part_one_with_input(self):
    self.assertEqual(11327140210986, part_one(program=self.input))

  def test_apply_mask2_example1(self):
    self.assertEqual('000000000000000000000000000000X1101X',
                     apply_mask2(mask='000000000000000000000000000000X1001X',
                                value=42))

  def test_apply_mask2_example2(self):
    self.assertEqual('00000000000000000000000000000001X0XX',
                     apply_mask2(mask='00000000000000000000000000000000X0XX',
                                value=26))

  def test_calculate_address_example1(self):
    self.assertCountEqual([26, 27, 58, 59], calculate_addresses(
        masked_address='000000000000000000000000000000X1101X'))

  def test_calculate_address_example2(self):
    self.assertCountEqual([16, 17, 18, 19, 24, 25, 26, 27], calculate_addresses(
        masked_address='00000000000000000000000000000001X0XX'))

  def test_part_two_with_example(self):
    self.assertEqual(208, part_two(program=self.examples[1]))

  def test_part_two_with_input(self):
    self.assertEqual(2308180581795, part_two(program=self.input))


if __name__ == '__main__':
  unittest.main()

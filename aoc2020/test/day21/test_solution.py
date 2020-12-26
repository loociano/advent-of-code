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
from aoc2020.src.day21.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example(self):
    self.assertEqual(5, part_one(self.examples[0]))

  def test_part_one_with_input(self):
    self.assertEqual(2542, part_one(self.input))

  def test_part_two_with_example(self):
    self.assertEqual('mxmxvkd,sqjhc,fvjkl', part_two(self.examples[0]))

  def test_part_two_with_input(self):
    self.assertEqual('hkflr,ctmcqjf,bfrq,srxphcm,snmxl,zvx,bd,mqvk',
                     part_two(self.input))


if __name__ == '__main__':
  unittest.main()
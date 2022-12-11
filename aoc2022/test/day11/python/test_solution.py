# Copyright 2022 Google LLC
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

from aoc2022.src.day11.python.solution import calc_monkey_business
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay11Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay11Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsMonkeyBusiness(self):
    self.assertEqual(10605, calc_monkey_business(self.examples[0]))

  def test_part1_withPuzzleInput_returnsMonkeyBusiness(self):
    self.assertEqual(57838, calc_monkey_business(self.input))


if __name__ == '__main__':
  unittest.main()

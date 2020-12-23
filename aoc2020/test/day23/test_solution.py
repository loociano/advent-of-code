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

from aoc2020.src.day23.solution import part_one, part_two
from aoc2020.test.common.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example(self):
    self.assertEqual('92658374', part_one('389125467', moves=10))

  def test_part_one_with_example_100_moves(self):
    self.assertEqual('67384529', part_one('389125467', moves=100))

  def test_part_one_with_input_100_moves(self):
    self.assertEqual('68245739', part_one(self.input[0], moves=100))

  def test_part_two_with_example(self):
    self.assertEqual(149245887792, part_two('389125467', moves=10000000))


if __name__ == '__main__':
  unittest.main()

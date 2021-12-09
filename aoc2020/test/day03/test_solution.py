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

from aoc2020.src.day03.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def setUp(self):
    self.slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

  def test_part_one_with_example(self):
    self.assertEqual(7, part_one(tree_map=self.examples[0],
                                 slope_right=3, slope_down=1))

  def test_part_one_with_input(self):
     self.assertEqual(164, part_one(tree_map=self.input,
                                    slope_right=3, slope_down=1))

  def test_part_two_with_example(self):
    self.assertEqual(336, part_two(tree_map=self.examples[0], slopes=self.slopes))

  def test_part_two_with_input(self):
    self.assertEqual(5007658656, part_two(tree_map=self.input,
                                          slopes=self.slopes))


if __name__ == '__main__':
  unittest.main()

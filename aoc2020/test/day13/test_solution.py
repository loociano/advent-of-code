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
from aoc2020.src.day13.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example(self):
    self.assertEqual(295, part_one(timestamp=int(self.examples[0][0]),
                                   bus_ids=self.examples[0][1].split(',')))

  def test_part_one_with_input(self):
    self.assertEqual(3966, part_one(timestamp=int(self.input[0]),
                                   bus_ids=self.input[1].split(',')))

  def test_part_two_with_small_example1(self):
      self.assertEqual(3417, part_two(bus_ids=['17','x','13','19']))

  def test_part_two_with_small_example2(self):
      self.assertEqual(754018, part_two(bus_ids=['67','7','59','61']))

  def test_part_two_with_small_example3(self):
      self.assertEqual(779210, part_two(bus_ids=['67','x','7','59','61']))

  def test_part_two_with_small_example4(self):
      self.assertEqual(1261476, part_two(bus_ids=['67','7','x','59','61']))

  def test_part_two_with_small_example5(self):
      self.assertEqual(1202161486, part_two(bus_ids=['1789','37','47','1889']))

  def test_part_two_with_example(self):
      self.assertEqual(1068781,
                       part_two(bus_ids=self.examples[0][1].split(',')))

  def test_part_two_with_input(self):
      self.assertEqual(123,
                       part_two(bus_ids=self.input[1].split(',')))

if __name__ == '__main__':
  unittest.main()

# Copyright 2019 Google LLC
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
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase
from aoc2019.src.day12.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one(self):
    self.assertEqual(6735, part_one(moon_data=self.input, steps=1000))

  def test_part_two(self):
    self.assertEqual(326489627728984, part_two(moon_data=self.input))


if __name__ == '__main__':
  unittest.main()

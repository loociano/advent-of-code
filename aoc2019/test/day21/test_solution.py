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
from aoc2019.src.day21.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part_one(self):
    self.assertEqual(19357290, part_one(program=self.input[0]))

  def test_part_two(self):
    self.assertEqual(1136394042, part_two(program=self.input[0]))


if __name__ == '__main__':
  unittest.main()

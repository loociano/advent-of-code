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
from aoc2019.src.day08.solution import part_one, part_two


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one(self):
    self.assertEqual(1965, part_one(input=self.input[0], width=25, height=6))

  def test_part_two(self):
    self.assertEqual(''.join([
      ' XX  XXXX X  X   XX X   X\n',
      'X  X    X X X     X X   X\n',
      'X      X  XX      X  X X \n',
      'X XX  X   X X     X   X  \n',
      'X  X X    X X  X  X   X  \n',
      ' XXX XXXX X  X  XX    X  ']), part_two(input=self.input[0], width=25,
                                              height=6))  # GZKJY


if __name__ == '__main__':
  unittest.main()

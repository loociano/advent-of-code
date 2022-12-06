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

from aoc2022.src.day06.python.solution import find_marker_position
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay06Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay06Solution, self).__init__(
      __file__, read_raw=True, *args, **kwargs)

  def test_part1_withExampleInput_returnsMessage(self):
    self.assertEqual(7, find_marker_position(self.examples[0]))

  # TODO: parameterize.
  def test_part1_withExampleInput2_returnsMessage(self):
    self.assertEqual(5, find_marker_position(self.examples[1]))

  def test_part1_withExampleInput3_returnsMessage(self):
    self.assertEqual(6, find_marker_position(self.examples[2]))

  def test_part1_withExampleInput4_returnsMessage(self):
    self.assertEqual(10, find_marker_position(self.examples[3]))

  def test_part1_withExampleInput5_returnsMessage(self):
    self.assertEqual(11, find_marker_position(self.examples[4]))

  def test_part1_withPuzzleInput_returnsMessage(self):
    self.assertEqual(1833, find_marker_position(self.input))


if __name__ == '__main__':
  unittest.main()

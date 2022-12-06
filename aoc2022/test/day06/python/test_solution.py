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

  def test_part1_withExampleInput1_returnsMessage(self):
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

  def test_part2_withExampleInput1_returnsMessage(self):
    self.assertEqual(19, find_marker_position(self.examples[0], marker_size=14))

  # TODO: parameterize.
  def test_part2_withExampleInput2_returnsMessage(self):
    self.assertEqual(23, find_marker_position(self.examples[1], marker_size=14))

  def test_part2_withExampleInput3_returnsMessage(self):
    self.assertEqual(23, find_marker_position(self.examples[2], marker_size=14))

  def test_part2_withExampleInput4_returnsMessage(self):
    self.assertEqual(29, find_marker_position(self.examples[3], marker_size=14))

  def test_part2_withExampleInput5_returnsMessage(self):
    self.assertEqual(26, find_marker_position(self.examples[4], marker_size=14))

  def test_part2_withPuzzleInput_returnsMessage(self):
    self.assertEqual(3425, find_marker_position(self.input, marker_size=14))


if __name__ == '__main__':
  unittest.main()

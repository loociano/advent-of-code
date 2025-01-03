# Copyright 2024 Google LLC
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
from aoc2024.src.day09.python.solution import checksum


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_part1_withExample_checksums(self):
    self.assertEqual(60, checksum('12345'))

  def test_part1_withExample2_checksums(self):
    self.assertEqual(1928, checksum('2333133121414131402'))

  def test_part1_withPuzzleInput_checksums(self):
    self.assertEqual(6448989155953, checksum(self.input[0]))

  def test_part2_withExample_checksums(self):
    self.assertEqual(132, checksum('12345', move_whole_files=True))

  def test_part2_withExample2_checksums(self):
    self.assertEqual(2858, checksum('2333133121414131402', move_whole_files=True))

  def test_part2_withPuzzleInput_checksums(self):
    self.assertEqual(6476642796832, checksum(self.input[0], move_whole_files=True))


if __name__ == '__main__':
  unittest.main()

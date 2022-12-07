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

from aoc2022.src.day07.python.solution import sum_directory_sizes, \
  smallest_dir_size_to_delete
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay07Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay07Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsSize(self):
    self.assertEqual(95437, sum_directory_sizes(self.examples[0]))

  def test_part1_withPuzzleInput_returnsSize(self):
    self.assertEqual(1513699, sum_directory_sizes(self.input))

  def test_part2_withExampleInput_returnsSize(self):
    self.assertEqual(24933642, smallest_dir_size_to_delete(self.examples[0]))

  def test_part2_withPuzzleInput_returnsSize(self):
    self.assertEqual(7991939, smallest_dir_size_to_delete(self.input))


if __name__ == '__main__':
  unittest.main()

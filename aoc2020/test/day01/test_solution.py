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

from common.file_utils import get_path, read_as_ints
from aoc2020.src.day01.solution import part_one, part_two


class TestDay01(unittest.TestCase):
  def setUp(self):
    self.example = read_as_ints(get_path(__file__, 'example.txt'))
    self.input = read_as_ints(get_path(__file__, 'input.txt'))

  def test_part_one_with_example(self):
    self.assertEqual(514579, part_one(self.example))

  def test_part_one_with_input(self):
    self.assertEqual(1009899, part_one(self.input))

  def test_part_two_with_example(self):
    self.assertEqual(241861950, part_two(self.example))

  def test_part_two_with_input(self):
    self.assertEqual(44211152, part_two(self.input))


if __name__ == '__main__':
  unittest.main()
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
from random import shuffle

from aoc2020.src.day09.solution import is_valid_xmas, part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_is_valid_xmas(self):
    preamble = list(range(1, 26))
    shuffle(preamble)
    self.assertTrue(is_valid_xmas(preamble, target=26))

  def test_is_valid_xmas1(self):
    preamble = list(range(1, 20)) + list(range(21, 26)) + [45]
    shuffle(preamble)
    self.assertTrue(is_valid_xmas(preamble, target=26))

  def test_is_valid_xmas2(self):
    preamble = list(range(1, 20)) + list(range(21, 26)) + [45]
    shuffle(preamble)
    self.assertTrue(is_valid_xmas(preamble, target=64))

  def test_is_valid_xmas3(self):
    preamble = list(range(1, 20)) + list(range(21, 26)) + [45]
    shuffle(preamble)
    self.assertFalse(is_valid_xmas(preamble, target=65))

  def test_is_valid_xmas4(self):
    preamble = list(range(1, 20)) + list(range(21, 26)) + [45]
    shuffle(preamble)
    self.assertTrue(is_valid_xmas(preamble, target=66))

  def test_part_one_with_example(self):
    self.assertEqual(127, part_one(
        preamble_size=5, xmas_data=list(map(int, self.examples[0]))))

  def test_part_one_with_input(self):
    self.assertEqual(1492208709, part_one(
        preamble_size=25, xmas_data=list(map(int, self.input))))

  def test_part_two_with_example(self):
    self.assertEqual(62, part_two(
        preamble_size=5, xmas_data=list(map(int, self.examples[0]))))

  def test_part_two_with_input(self):
    self.assertEqual(238243506, part_two(
        preamble_size=25, xmas_data=list(map(int, self.input))))

if __name__ == '__main__':
  unittest.main()

# Copyright 2025 Google LLC
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

from aoc2025.src.day02.python.solution import is_valid_id, find_invalid_ids, find_all_invalid_ids
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class ValidationIdTest(unittest.TestCase):
  def test_validIds(self):
    self.assertTrue(is_valid_id('123'))
    self.assertTrue(is_valid_id('1'))
    self.assertTrue(is_valid_id('101'))

  def test_invalidIds(self):
    self.assertFalse(is_valid_id('55'))
    self.assertFalse(is_valid_id('6464'))
    self.assertFalse(is_valid_id('123123'))


class InvalidIdFindingTest(unittest.TestCase):
  def test_findInvalidIds(self):
    self.assertEqual((11, 22), find_invalid_ids(range(11, 23)))
    self.assertEqual((99,), find_invalid_ids(range(95, 116)))
    self.assertEqual((1010,), find_invalid_ids(range(998, 1013)))
    self.assertEqual((1188511885,), find_invalid_ids(range(1188511880, 1188511891)))
    self.assertEqual((222222,), find_invalid_ids(range(222220, 222225)))
    self.assertEqual((), find_invalid_ids(range(1698522, 1698529)))
    self.assertEqual((446446,), find_invalid_ids(range(446443, 446450)))
    self.assertEqual((38593859,), find_invalid_ids(range(38593856, 38593863)))
    self.assertEqual((), find_invalid_ids(range(565653, 565660)))
    self.assertEqual((), find_invalid_ids(range(824824821, 824824828)))
    self.assertEqual((), find_invalid_ids(range(2121212118, 2121212125)))


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_addAllInvalidIds_withSampleInput(self):
    self.assertEqual(1227775554, sum(find_all_invalid_ids(id_ranges=self.examples[0][0])))

  def test_addAllInvalidIds_withPuzzleInput(self):
    self.assertEqual(24157613387, sum(find_all_invalid_ids(id_ranges=self.input[0])))


if __name__ == '__main__':
  unittest.main()

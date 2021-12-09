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

from aoc2020.src.day25.solution import find_loop_size, part_one
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_find_loop_size(self):
    self.assertEqual(8, find_loop_size(5764801))
    self.assertEqual(11, find_loop_size(17807724))

  def test_part_one_with_example(self):
    self.assertEqual(14897079, part_one(card_public_key=5764801,
                                        door_public_key=17807724))

  def test_part_one_with_input(self):
    self.assertEqual(12285001, part_one(card_public_key=17607508,
                                        door_public_key=15065270))


if __name__ == '__main__':
  unittest.main()

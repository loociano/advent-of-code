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
from aoc2019.src.day18.solution import part_one


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_shortest_path_test1(self):
    self.assertEqual(8, part_one(self.examples[0]))

  def test_shortest_path_test2(self):
    self.assertEqual(86, part_one(self.examples[1]))

  def test_shortest_path_test3(self):
    self.assertEqual(132, part_one(self.examples[2]))


if __name__ == '__main__':
  unittest.main()

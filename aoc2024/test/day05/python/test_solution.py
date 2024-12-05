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

from aoc2024.src.day05.python.solution import sum_middle_pages
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay05Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestDay05Solution, self).__init__(__file__, *args, **kwargs))

  def test_part1_withExample_sums(self):
    self.assertEqual(143, sum_middle_pages(self.examples[0]))

  def test_part1_withPuzzleInput_sums(self):
    self.assertEqual(7024, sum_middle_pages(self.input))


if __name__ == '__main__':
  unittest.main()

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

from aoc2025.src.day06.python.solution import calculate_grand_total, parse_lines2
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def testPart1_withSampleInput(self):
    self.assertEqual(4277556, calculate_grand_total(self.examples[0]))

  def testPart1_withPuzzleInput(self):
    self.assertEqual(4449991244405, calculate_grand_total(self.input))

  def testPart2_withSampleInput(self):
    self.assertEqual(3263827, calculate_grand_total(self.examples[0],
                                                    parse_fn=parse_lines2))

  def testPart2_withPuzzleInput(self):
    self.assertEqual(9348430857627, calculate_grand_total(self.input,
                                                    parse_fn=parse_lines2))


if __name__ == '__main__':
  unittest.main()

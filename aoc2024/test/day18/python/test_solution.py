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
from aoc2024.src.day18.python.solution import min_steps_to_exit, find_first_byte_preventing_exit


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_success(self):
    self.assertEqual(22, min_steps_to_exit(self.examples[0], num_bytes=12, width=7, length=7))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual(234, min_steps_to_exit(self.input, num_bytes=1024))

  def test_part2_withExample_success(self):
    self.assertEqual((6, 1), find_first_byte_preventing_exit(self.examples[0], width=7, length=7))

  def test_part2_withPuzzleInput_success(self):
    self.assertEqual((58, 19), find_first_byte_preventing_exit(self.input))


if __name__ == '__main__':
  unittest.main()

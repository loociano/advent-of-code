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

from aoc2024.src.day02.python.solution import num_safe_reports
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay01Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay01Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExample_getsNumSafeReports(self):
    self.assertEqual(2, num_safe_reports(self.examples[0]))

  def test_part1_withPuzzleInput_getsNumSafeReports(self):
    self.assertEqual(299, num_safe_reports(self.input))

  def test_part2_withExample_getsNumSafeReports(self):
    self.assertEqual(4, num_safe_reports(self.examples[0], tolerate_bad_level=True))

  def test_part2_withPuzzleInput_getsNumSafeReports(self):
    self.assertEqual(364, num_safe_reports(self.input, tolerate_bad_level=True))


if __name__ == '__main__':
  unittest.main()

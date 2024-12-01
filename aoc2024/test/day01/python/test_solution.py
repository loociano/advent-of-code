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

from aoc2024.src.day01.python.solution import calculate_distance, calculate_similarity_score
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay01Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay01Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExample_calculatesDistance(self):
    self.assertEqual(11, calculate_distance(self.examples[0]))

  def test_part1_withPuzzleInput_calculatesDistance(self):
    self.assertEqual(1834060, calculate_distance(self.input))

  def test_part2_withExample_calculatesSimilarityScore(self):
    self.assertEqual(31, calculate_similarity_score(self.examples[0]))

  def test_part2_withPuzzleInput_calculatesSimilarityScore(self):
    self.assertEqual(21607792, calculate_similarity_score(self.input))


if __name__ == '__main__':
  unittest.main()

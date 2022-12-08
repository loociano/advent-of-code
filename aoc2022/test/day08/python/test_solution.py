# Copyright 2022 Google LLC
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

from aoc2022.src.day08.python.solution import count_visible_trees, \
  find_max_scenic_score
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay08Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay08Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsVisibleTrees(self):
    self.assertEqual(21, count_visible_trees(self.examples[0]))

  def test_part1_withPuzzleInput_returnsVisibleTrees(self):
    self.assertEqual(1809, count_visible_trees(self.input))

  def test_part2_withExampleInput_returnsMaxScenicScore(self):
    self.assertEqual(8, find_max_scenic_score(self.examples[0]))

  def test_part2_withPuzzleInput_returnsMaxScenicScore(self):
    self.assertEqual(479400, find_max_scenic_score(self.input))


if __name__ == '__main__':
  unittest.main()

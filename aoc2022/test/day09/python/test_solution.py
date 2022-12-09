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

from aoc2022.src.day09.python.solution import count_tail_visited_positions
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay09Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay09Solution, self).__init__(__file__, *args, **kwargs)

  def test_part1_withExampleInput_returnsVisibleTrees(self):
    self.assertEqual(13, count_tail_visited_positions(self.examples[0]))

  def test_part1_withPuzzleInput_returnsVisibleTrees(self):
    self.assertEqual(6175, count_tail_visited_positions(self.input))


if __name__ == '__main__':
  unittest.main()
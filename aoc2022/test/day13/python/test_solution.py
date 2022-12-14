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

from aoc2022.src.day13.python.solution import is_correct_order, \
  sum_indices_correct_order
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay13Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay13Solution, self).__init__(__file__, *args, **kwargs)

  def test_checkOrder_withIntegerLists_correctOrder(self):
    self.assertTrue(
      is_correct_order(left=[1, 1, 3, 1, 1], right=[1, 1, 5, 1, 1]))

  def test_checkOrder_withListAndInteger_correctOrder(self):
    self.assertTrue(
      is_correct_order(left=[[1], [2, 3, 4]], right=[[1], 4]))

  def test_checkOrder_withListAndInteger_incorrectOrder(self):
    self.assertFalse(
      is_correct_order(left=[9], right=[[8, 7, 6]]))

  def test_checkOrder_withLeftOutOfItems_correctOrder(self):
    self.assertTrue(
      is_correct_order(left=[[4, 4], 4, 4], right=[[4, 4], 4, 4, 4]))

  def test_checkOrder_withRightOutOfItems_incorrectOrder(self):
    self.assertFalse(
      is_correct_order(left=[7, 7, 7, 7], right=[7, 7, 7]))

  def test_checkOrder_withEmptyLeft_correctOrder(self):
    self.assertTrue(
      is_correct_order(left=[], right=[3]))

  def test_checkOrder_withAllEmptyRightOutOfItems_incorrectOrder(self):
    self.assertFalse(
      is_correct_order(left=[[[]]], right=[[]]))

  def test_checkOrder_withRightSmaller_incorrectOrder(self):
    self.assertFalse(
      is_correct_order(left=[1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                       right=[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]))

  def test_part1_withExampleInput_detectsCorrectPairs(self):
    self.assertEqual(13, sum_indices_correct_order(self.examples[0]))

  def test_part1_withPuzzleInput_detectsCorrectPairs(self):
    self.assertEqual(6428, sum_indices_correct_order(self.input))


if __name__ == '__main__':
  unittest.main()

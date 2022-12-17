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

from aoc2022.src.day15.python.solution import get_manhattan_distance, count_not_beacon_positions
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestDay15Solution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestDay15Solution, self).__init__(__file__, *args, **kwargs)

  def test_manhattanDistance_success(self):
    self.assertEqual(7, get_manhattan_distance(position_a=(2, 18), position_b=(-2, 15)))
    self.assertEqual(1, get_manhattan_distance(position_a=(9, 16), position_b=(10, 16)))
    self.assertEqual(3, get_manhattan_distance(position_a=(13, 2), position_b=(15, 3)))
    self.assertEqual(4, get_manhattan_distance(position_a=(12, 14), position_b=(10, 16)))
    self.assertEqual(4, get_manhattan_distance(position_a=(10, 20), position_b=(10, 16)))
    self.assertEqual(5, get_manhattan_distance(position_a=(14, 17), position_b=(10, 16)))
    self.assertEqual(9, get_manhattan_distance(position_a=(8, 7), position_b=(2, 10)))
    # Also...
    # Sensor at x=2, y=0: closest beacon is at x=2, y=10
    # Sensor at x=0, y=11: closest beacon is at x=2, y=10
    # Sensor at x=20, y=14: closest beacon is at x=25, y=17
    # Sensor at x=17, y=20: closest beacon is at x=21, y=22
    # Sensor at x=16, y=7: closest beacon is at x=15, y=3
    # Sensor at x=14, y=3: closest beacon is at x=15, y=3
    # Sensor at x=20, y=1: closest beacon is at x=15, y=3

  def test_simulateSandFall_withExample_correctCount(self):
    self.assertEqual(26, count_not_beacon_positions(self.examples[0], row=10))

  def test_simulateSandFall_withPuzzleInput_correctCount(self):
    self.assertEqual(5112034, count_not_beacon_positions(self.input, row=2000000))


if __name__ == '__main__':
  unittest.main()

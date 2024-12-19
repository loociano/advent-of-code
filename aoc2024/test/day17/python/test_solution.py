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
from aoc2024.src.day17.python.solution import print_stdout, find_reg_a_init_value


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_success(self):
    self.assertEqual('4,6,3,5,6,3,5,2,1,0', print_stdout(self.examples[0]))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual('2,0,1,3,4,0,2,1,7', print_stdout(self.input))

  def test_part2_withExample_success(self):
    self.assertEqual(117440, find_reg_a_init_value(self.examples[1]))

  def test_part2_withPuzzleInput_success(self):
    # bst,A
    # bxl,3
    # cdv,B
    # adv,3
    # bxc
    # bxl,5
    # out,B
    # jnz,0
    # Desired output: 2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0
    # self.assertEqual(???, find_reg_a_init_value(self.input))
    pass


if __name__ == '__main__':
  unittest.main()

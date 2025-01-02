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
from aoc2024.src.day24.python.solution import get_output, find_wrong_output_wires


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    (super(TestSolution, self).__init__(__file__, *args,
                                        **kwargs))

  def test_part1_withExample_success(self):
    self.assertEqual(4, get_output(self.examples[0]))

  def test_part1_withExample2_success(self):
    self.assertEqual(2024, get_output(self.examples[1]))

  def test_part1_withPuzzleInput_success(self):
    self.assertEqual(36035961805936, get_output(self.input))

  def test_part2_withExample_success(self):
    self.assertEqual('z00,z01,z02,z05', find_wrong_output_wires(self.examples[2],
                                                                swaps=(('z00', 'z05'),
                                                                       ('z01', 'z02'))))

  def test_part2_withPuzzleInput_success(self):
    # The input is a Ripple Carry Adder!
    # Output has 44 bits + carry.
    # https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
    # Generated Graphviz DOT and inspected the diagram looking for incorrect connections.
    # Rules:
    # 1. Signal z = (x XOR y) XOR Cin.
    # 2. Cout = (x AND y) OR (Cin AND (x XOR y))
    self.assertEqual('jqf,mdd,skh,wpd,wts,z11,z19,z37', find_wrong_output_wires(self.input,
                                                                                swaps=(('z11', 'wpd'),
                                                                                       ('skh', 'jqf'),
                                                                                       ('z19', 'mdd'),
                                                                                       ('z37', 'wts')),
                                                                                operation='+'))


if __name__ == '__main__':
  unittest.main()

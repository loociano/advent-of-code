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

from aoc2024.src.day17.python.computer import Computer


class TestComputer(unittest.TestCase):

  def test_computer_bst_success(self):
    computer = Computer(program=(2, 6), reg_c=9)
    computer.execute()
    self.assertEqual(1, computer.reg_b)

  def test_computer_program1_success(self):
    computer = Computer(program=(5, 0, 5, 1, 5, 4), reg_a=10)
    computer.execute()
    self.assertEqual('0,1,2', computer.flush())

  def test_computer_program2_success(self):
    """
    adv 1
    out A
    jnz 0
    """
    computer = Computer(program=(0, 1, 5, 4, 3, 0), reg_a=2024)
    computer.execute()

    self.assertEqual('4,2,5,6,7,7,7,7,3,1,0', computer.flush())
    self.assertEqual(0, computer.reg_a)

  def test_computer_program3_success(self):
    computer = Computer(program=(1, 7), reg_b=29)
    computer.execute()
    self.assertEqual(26, computer.reg_b)

  def test_computer_program4_success(self):
    computer = Computer(program=(4,0), reg_b=2024, reg_c=43690)
    computer.execute()
    self.assertEqual(44354, computer.reg_b)


if __name__ == '__main__':
  unittest.main()

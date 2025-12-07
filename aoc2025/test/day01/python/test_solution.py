# Copyright 2025 Google LLC
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

from aoc2025.src.day01.python.solution import Dial, find_password
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class DialTest(unittest.TestCase):
  def testDial_defaultStartPosition_success(self):
    self.assertEqual(50, Dial().position)

  def testDial_validStartPosition_success(self):
    self.assertEqual(0, Dial(start_position=0).position)

  def testDial_invalidStartPosition_fails(self):
    with self.assertRaises(ValueError) as cm:
      Dial(start_position=-1)
    self.assertEqual('Start position must be between 0 and 99, was: -1',
                     cm.exception.args[0])
    with self.assertRaises(ValueError) as cm:
      Dial(start_position=100)
    self.assertEqual('Start position must be between 0 and 99, was: 100',
                     cm.exception.args[0])

  def testDial_rotatePositive_success(self):
    dial = Dial()
    dial.rotate(1)
    self.assertEqual(51, dial.position)

  def testDial_rotateNegative_success(self):
    dial = Dial()
    dial.rotate(-1)
    self.assertEqual(49, dial.position)

  def testDial_rotateBeyondBounds_success(self):
    dial = Dial()
    dial.rotate(-51)
    self.assertEqual(99, dial.position)
    dial.rotate(1)
    self.assertEqual(0, dial.position)

  def testDial_rotate1round_success(self):
    dial = Dial(start_position=0)
    dial.rotate(-100)
    self.assertEqual(0, dial.position)
    dial.rotate(100)
    self.assertEqual(0, dial.position)

  def testDial_rotateMultipleRounds_success(self):
    dial = Dial(start_position=0)
    dial.rotate(-201)
    self.assertEqual(99, dial.position)

  def testDial_countZeroClicks_success(self):
    dial = Dial()
    self.assertEqual(1, dial.rotate(-68))
    self.assertEqual(82, dial.position)
    self.assertEqual(0, dial.rotate(-30))
    self.assertEqual(52, dial.position)
    self.assertEqual(1, dial.rotate(48))
    self.assertEqual(0, dial.position)
    self.assertEqual(1, dial.rotate(100))
    self.assertEqual(0, dial.position)
    self.assertEqual(0, dial.rotate(-1))
    self.assertEqual(99, dial.position)

  def testDial_countZeroClicksMultipleNegativeRotations_success(self):
    dial = Dial()
    self.assertEqual(10, dial.rotate(-1000))
    self.assertEqual(50, dial.position)

  def testDial_countZeroClicksMultiplePositiveRotations_success(self):
    dial = Dial()
    self.assertEqual(10, dial.rotate(1000))
    self.assertEqual(50, dial.position)

  def testDial_countCrossingsWhenStartingAtZero_success(self):
    dial = Dial(start_position=0)
    self.assertEqual(0, dial.rotate(-1))
    self.assertEqual(99, dial.position)
    self.assertEqual(1, dial.rotate(100))
    self.assertEqual(99, dial.position)
    self.assertEqual(10, dial.rotate(1000))
    self.assertEqual(99, dial.position)

  def testDial_countCrossingsEdgeCase_success(self):
    dial = Dial()
    self.assertEqual(1, dial.rotate(-50))
    self.assertEqual(0, dial.position)
    self.assertEqual(1, dial.rotate(101))
    self.assertEqual(1, dial.position)


class TestDaySolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super().__init__(__file__, *args, **kwargs)

  def test_findPassword_withInvalidInput_fails(self):
    with self.assertRaises(ValueError) as cm:
      find_password(rotations=('foo',))
    self.assertEqual('Invalid rotation foo, expected format [LR]\\d+',
                     cm.exception.args[0])

  def test_findPassword_withSampleInput(self):
    self.assertEqual(3, find_password(self.examples[0]))

  def test_findPassword_withPuzzleInput(self):
    self.assertEqual(1168, find_password(self.input))

  def test_findPasswordMethod0x434C49434B_withSampleInput(self):
    self.assertEqual(6, find_password(self.examples[0], count_all_zero_clicks=True))

  def test_findPasswordMethod0x434C49434B_edgeCases(self):
    self.assertEqual(1, find_password(('L50', 'R50'), count_all_zero_clicks=True))
    self.assertEqual(1, find_password(('L50', 'L50'), count_all_zero_clicks=True))
    self.assertEqual(1, find_password(('R50', 'L50'), count_all_zero_clicks=True))
    self.assertEqual(1, find_password(('R50', 'R50'), count_all_zero_clicks=True))
    self.assertEqual(2, find_password(('L150', 'L50'), count_all_zero_clicks=True))
    self.assertEqual(2, find_password(('L150', 'R50'), count_all_zero_clicks=True))
    self.assertEqual(2, find_password(('R150', 'L50'), count_all_zero_clicks=True))
    self.assertEqual(2, find_password(('R150', 'R50'), count_all_zero_clicks=True))

  def test_findPasswordMethod0x434C49434B_withPuzzleInput(self):
    self.assertEqual(7199, find_password(self.input, count_all_zero_clicks=True))


if __name__ == '__main__':
  unittest.main()

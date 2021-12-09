# Copyright 2020 Google LLC
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

from aoc2020.src.day16.solution import part_one, part_two, parse_notes, \
  find_field_order
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
  def __init__(self, *args, **kwargs):
    super(TestSolution, self).__init__(__file__, *args, **kwargs)

  def test_part_one_with_example1(self):
    self.assertEqual(71, part_one(notes=self.examples[0]))

  def test_part_one_with_input(self):
    self.assertEqual(23954, part_one(notes=self.input))

  def test_find_field_order_with_example2(self):
    nearby_tickets, your_ticket, rules = parse_notes(self.examples[1])
    # There are no invalid tickets in this example.
    self.assertEqual(['row', 'class', 'seat'],
                     find_field_order(nearby_tickets, rules))

  def test_part_two_with_input(self):
    self.assertEqual(453459307723, part_two(notes=self.input))


if __name__ == '__main__':
  unittest.main()

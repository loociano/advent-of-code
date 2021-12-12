# Copyright 2021 Google LLC
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

from aoc2021.src.day06.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(__file__, *args, **kwargs)

    def test_part_one_with_example(self):
        self.assertEqual(26,
                         part_one(lanternfish_ages=self.examples[0], days=18))
        self.assertEqual(5934,
                         part_one(lanternfish_ages=self.examples[0], days=80))

    def test_part_one_with_input(self):
        self.assertEqual(349549,
                         part_one(lanternfish_ages=self.input, days=80))

    def test_part_two_with_example(self):
        self.assertEqual(26984457539,
                         part_two(lanternfish_ages=self.examples[0], days=256))

    def test_part_two_with_input(self):
        self.assertEqual(1589590444365,
                         part_two(lanternfish_ages=self.input, days=256))


if __name__ == '__main__':
    unittest.main()

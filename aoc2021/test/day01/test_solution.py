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

from aoc2021.src.day01.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


class TestSolution(AdventOfCodeTestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(__file__, *args, **kwargs)

    def setUp(self):
        self._example = tuple(map(int, self.examples[0]))
        self._input = tuple(map(int, self.input))

    def test_part_one_with_example(self):
        self.assertEqual(7, part_one(self._example))

    def test_part_one_with_input(self):
        self.assertEqual(1154, part_one(self._input))

    def test_part_two_with_example(self):
        self.assertEqual(5, part_two(self._example))

    def test_part_two_with_input(self):
        self.assertEqual(1127, part_two(self._input))


if __name__ == '__main__':
    unittest.main()

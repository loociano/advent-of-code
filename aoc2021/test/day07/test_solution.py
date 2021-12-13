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
from typing import Sequence

from aoc2021.src.day07.solution import part_one, part_two
from common.python3.AdventOfCodeTestCase import AdventOfCodeTestCase


def _process_input(input_file: str) -> Sequence[int]:
    return tuple(map(int, input_file[0].split(',')))


class TestSolution(AdventOfCodeTestCase):
    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(__file__, *args, **kwargs)

    def setUp(self) -> None:
        self._example = _process_input(input_file=self.examples[0])
        self._input = _process_input(input_file=self.input)

    def test_part_one_with_example(self):
        self.assertEqual(37, part_one(positions=self._example))

    def test_part_one_with_input(self):
        self.assertEqual(352254, part_one(positions=self._input))

    def test_part_two_with_example(self):
        self.assertEqual(168, part_two(positions=self._example))

    def test_part_two_with_input(self):
        self.assertEqual(999, part_two(positions=self._input))


if __name__ == '__main__':
    unittest.main()

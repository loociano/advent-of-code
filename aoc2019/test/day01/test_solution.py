# Copyright 2019 Google LLC
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

from aoc2019.src.common.utils import get_path
from aoc2019.src.day01.solution import part_one, part_two


class TestDay01(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(3246455, part_one(get_path(__file__, 'input.txt')))

    def test_part_two(self):
        self.assertEqual(4866824, part_two(get_path(__file__, 'input.txt')))


if __name__ == '__main__':
    unittest.main()

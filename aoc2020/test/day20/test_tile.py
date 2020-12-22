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

from aoc2020.src.day20.Tile import Tile


class TestSolution(unittest.TestCase):

  def test_rotate_right(self):
    tile = Tile(tile_id=123, image=[
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']])
    tile.rotate_right()
    self.assertListEqual([
        ['g', 'd', 'a'],
        ['h', 'e', 'b'],
        ['i', 'f', 'c']], tile.image)

  def test_flip(self):
    tile = Tile(tile_id=123, image=[
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']])
    tile.vertical_flip()
    self.assertListEqual([
        ['c', 'b', 'a'],
        ['f', 'e', 'd'],
        ['i', 'h', 'g']], tile.image)


if __name__ == '__main__':
  unittest.main()

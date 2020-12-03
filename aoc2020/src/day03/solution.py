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
from functools import reduce

TREE = '#'


def part_one(tree_map: list, slope_right: int, slope_down) -> int:
  return _count_trees(tree_map=tree_map,
                      slope_right=slope_right, slope_down=slope_down)


def part_two(tree_map: list, slopes: list):
  return reduce(
      lambda x, y: x * y,
      [_count_trees(tree_map=tree_map,
                    slope_right=slope[0],
                    slope_down=slope[1]) for slope in slopes],
      1)


def _count_trees(tree_map: list, slope_right: int, slope_down: int) -> int:
  num_trees = 0
  x = 0
  WIDTH = len(tree_map[0])

  for y in range(0, len(tree_map), slope_down):
    if tree_map[y][x % WIDTH] == TREE:
      num_trees += 1
    x += slope_right
  return num_trees

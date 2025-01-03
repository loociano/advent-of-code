# Copyright 2022 Google LLC
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
from typing import Sequence, Tuple


def _is_visible_from_edge(forest: Sequence[Sequence[int]], x: int, y: int,
                          direction: Tuple[int, int]) -> bool:
  curr_x = x
  curr_y = y
  while 0 < curr_x < len(forest) - 1 and 0 < curr_y < len(forest[0]) - 1:
    if forest[curr_x + direction[0]][curr_y + direction[1]] >= forest[x][y]:
      return False
    curr_x += direction[0]
    curr_y += direction[1]
  return True


def _is_visible(forest: Sequence[Sequence[int]], x: int, y: int) -> bool:
  if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest[0]) - 1:
    return True  # Edge trees are visible.
  for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    if _is_visible_from_edge(forest, x, y, direction):
      return True
  return False


def _calc_scenic_score_in_dir(forest: Sequence[Sequence[int]], x: int, y: int,
                              direction: Tuple[int, int]) -> int:
  curr_x = x
  curr_y = y
  count_trees = 0
  while 0 < curr_x < len(forest) - 1 and 0 < curr_y < len(forest[0]) - 1:
    count_trees += 1
    if forest[curr_x + direction[0]][curr_y + direction[1]] >= forest[x][y]:
      return count_trees
    curr_x += direction[0]
    curr_y += direction[1]
  return count_trees


def _calc_scenic_score(forest: Sequence[Sequence[int]], x: int, y: int) -> int:
  if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest[0]) - 1:
    return 0
  scenic_score = 1
  for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    scenic_score *= _calc_scenic_score_in_dir(forest, x, y, direction)
  return scenic_score


def count_visible_trees(forest_rows: Sequence[str]) -> int:
  forest = [list(map(int, list(row))) for row in forest_rows]
  visible_trees = 0
  for x in range(len(forest)):
    for y in range(len(forest[x])):
      visible_trees += _is_visible(forest, x, y)
  return visible_trees


def find_max_scenic_score(forest_rows: Sequence[str]) -> int:
  forest = [list(map(int, list(row))) for row in forest_rows]
  max_scenic_score = 0
  for x in range(len(forest)):
    for y in range(len(forest[x])):
      scenic_score = _calc_scenic_score(forest, x, y)
      if scenic_score > max_scenic_score:
        max_scenic_score = scenic_score
  return max_scenic_score

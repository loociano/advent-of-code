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
from typing import Sequence
from functools import cache
from common.python3.types import Position

_START = 'S'
_BEAM = '|'
_SPLIT = '^'
_SPACE = '.'


def count_beam_splits(grid: Sequence[Sequence[str]]) -> int:
  """Counts the number of splits a tachyon beam takes from start downwards."""
  mutable_grid = list(list(row) for row in grid)
  width = len(mutable_grid[0])  # Assumes all lines have same length.
  count_splits = 0
  for y in range(1, len(mutable_grid)):
    for x in range(0, width):
      if mutable_grid[y - 1][x] == _START and mutable_grid[y][x] == _SPACE:
        mutable_grid[y][x] = _BEAM
      if mutable_grid[y - 1][x] == _BEAM and mutable_grid[y][x] == _SPACE:
        mutable_grid[y][x] = _BEAM
      if mutable_grid[y - 1][x] == _BEAM and mutable_grid[y][x] == _SPLIT:
        count_splits += 1
        if x > 0:
          mutable_grid[y][x - 1] = _BEAM  # Split left
        if x < width - 1:
          mutable_grid[y][x + 1] = _BEAM  # Split right
  return count_splits


@cache  # Caches distinct paths from each split.
def _count_distinct_paths(grid: Sequence[Sequence[str]], pos: Position,
                          counter: int) -> int:
  """Recursively count distinct paths a tachyon can take.

  A tachyon always travels downwards. If it encounters a split '^', the tachyon
  can go either down-left or down-right.
  """
  if pos[0] == len(grid) - 1:
    return 1
  look_down = grid[pos[0] + 1][pos[1]]
  if look_down == _SPLIT:
    subcounter = 0
    # There are two possible downward directions: down-left or down-right
    for step in ((1, -1), (1, 1)):
      next_pos = (pos[0] + step[0]), (pos[1] + step[1])
      if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
        subcounter += _count_distinct_paths(grid=grid, pos=next_pos,
                                            counter=counter)
    return subcounter
  else:  # Must be empty space.
    # Can only go down.
    return _count_distinct_paths(grid=grid, pos=(pos[0] + 1, pos[1]),
                                 counter=counter)


def count_timelines(grid: Sequence[Sequence[str]]) -> int:
  """Counts the different timelines that a tachyon particle ends up on."""
  start_pos: Position = (0, list(grid[0]).index(_START))
  return _count_distinct_paths(grid=grid, pos=start_pos, counter=0)

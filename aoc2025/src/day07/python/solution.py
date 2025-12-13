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

_START = 'S'
_BEAM = '|'
_SPLIT = '^'
_SPACE = '.'


def count_beam_splits(grid: Sequence[Sequence[str]]) -> int:
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
